#include <stdio.h>
#include <stdlib.h>

#define ARRLEN(ARR) sizeof(ARR)/sizeof(ARR[0])

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* t1;
    struct ListNode* t2;
    t1 = l1;
    t2 = l2;

    int plus = 0;
    int t1Val = 0;
    int t2Val = 0;
    while (t1 != NULL || t2 != NULL) {
        t1Val = t1->val;
        t2Val = t2 == NULL ? 0 : t2->val;

        plus = t1Val + t2Val; 
        if (t1->next == NULL && ((plus / 10) || (t2 != NULL && t2->next != NULL))) {
            struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
            node->next = NULL;
            t1->next = node;
        }
        if (t1->next != NULL && (plus / 10)) {
            t1->next->val += plus / 10;
        }
        t1->val = (t1Val + t2Val) % 10;
        //t1可以保证不是NULL
        t1 = t1->next;
        t2 = t2 == NULL ? NULL : t2->next;
    }

    return l1;
}

void printList(struct ListNode* head) {
    struct ListNode *index = head;
    for (; index != NULL; index = index->next) {
        printf("%d ", index->val);
    }
}

struct ListNode* getNumList(int *l, int len) {
    int i = 0;
    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* index = head;
    index->val = l[0];
    index->next = NULL;

    for (i = 1; i < len; i++) {
        struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = l[i];
        node->next = NULL;
        index->next = node;
        index = node;
    }
    return head;
}

int main()
{
    int a[] = {2,0,7,0,9,4,6,2};
    int b[] = {0,8,9,2,6,6,4,9,9};

    int len_a = ARRLEN(a);
    int len_b = ARRLEN(b);

    struct ListNode* la = NULL;
    struct ListNode* lb = NULL;
    la = getNumList(a, len_a);
    lb = getNumList(b, len_b);

    printList(la);
    printf("\n");
    printList(lb);
    printf("\n");
    la = addTwoNumbers(la, lb);
    printList(la);
    return 0;
}
