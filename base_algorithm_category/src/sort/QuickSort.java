package sort;

public class QuickSort {

    public void sort(int[] data) {

        int left = 0;
        int right = data.length - 1;
        doSort(data, left, right);
    }

    private void doSort(int[]data, int left, int right) {
        if (left >= right) return;

        int j = partation(data, left, right);
        doSort(data, left, j - 1);
        doSort(data, j + 1, right);
    }

    private int partation(int[] data, int left, int right) {
        int pivot = data[left];
        int i = left + 1, j = right;
        while (i < j) {
            while (i < right && data[i] < pivot) ++i;
            while (j > left && data[j] > pivot) --j;
            if (i < j) {
                swap(data, i, j);
            }
        }
        swap(data, left, j);
        return j;
    }

    private void swap(int[]data, int i, int j) {
        int temp = data[i];
        data[i] = data[j];
        data[j] = temp;
    }

    public static void main(String[] args) {
        int[] data = new int[] {0, 9, 4, 1, 3, 2, 7, 6, 8, 5};
        data = new int[]{5, 9, 8, 7, 6, 4, 3, 2};
        (new QuickSort()).sort(data);
        for (int item : data) {
            System.out.print(item + " ");
        }
    }
}
