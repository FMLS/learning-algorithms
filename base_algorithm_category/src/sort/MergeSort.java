package sort;

public class MergeSort {

    public void sort(int[] data) {
        int[] aux = new int[data.length];
        doSort(data, 0, data.length - 1, aux);
    }

    private void doSort(int[] data, int lo, int hi, int[] aux) {
        if (lo >= hi) return;
        int mid = lo + (hi - lo) / 2;
        doSort(data, lo, mid, aux);
        doSort(data, mid + 1, hi, aux);
        merge(data, lo, mid, hi, aux);
    }

    private void merge(int[] data, int lo, int mid, int hi, int[] aux) {
        int i = lo;
        int j = mid + 1;

        for (int k = lo; k <= hi; ++k) {
            aux[k] = data[k];
        }

        for (int k = lo; k <= hi; ++k) {
            if (i > mid) data[k] = aux[j++];
            else if (j > hi) data[k] = aux[i++];
            else if (aux[j] < aux[i]) data[k] = aux[j++];
            else data[k] = aux[i++];
        }
    }

    public static void main(String[] args) {
        int[] data = new int[] {0, 9, 4, 1, 3, 2, 7, 6, 8, 5};
        (new MergeSort()).sort(data);
        for (int item : data) {
            System.out.print(item + " ");
        }
    }
}
