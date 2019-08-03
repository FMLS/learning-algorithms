package heap;

public class HeapSort<Key extends Comparable<Key>> {

    public void heapSort(Key[] data) {
        int N = data.length - 1;

        for (int i = N / 2; i >= 1; i--) {
            sink(data, i, N);
        }

        while (N > 1) {
            // 这两行需要注意, 先和最后一个元素交换, N--后再进行下沉操作
            exch(data, 1, N--);
            sink(data, 1, N);
        }
    }

    private void sink(Key[] data, int start, int end) {
        int i = start;
        int j;
        while (i * 2 <= end) {
            j = i * 2;
            // 这里要和两个子节点中较大者交换
            if (j < end && data[j].compareTo(data[j + 1]) < 0) j++;

            if (data[i].compareTo(data[j]) >= 0) break;
            exch(data, i, j);
            i = j;
        }
    }

    private void exch(Key[] data, int i, int j) {
        Key temp = data[i];
        data[i] = data[j];
        data[j] = temp;
    }

    public static void main(String[] args) {
        Integer[] data = new Integer[]{0, 7, 1, 0, 2, 4, 8, 9, 3, 6, 5};
        HeapSort<Integer> heapSort = new HeapSort<>();
        heapSort.heapSort(data);

        for (int i: data) {
            System.out.print(i);
            System.out.print(" ");
        }
    }
}
