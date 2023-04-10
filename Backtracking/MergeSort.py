def Merge(arr, copy_arr, left, right):
    mid = left + (right - left) // 2
    i, j, k = left, mid + 1, left
    while i <= mid or j <= right:
        if j > right or (i <= mid and arr[i] <= arr[j]):
            copy_arr[k] = arr[i]
            i += 1
        else:
            copy_arr[k] = arr[j]
            j += 1
        k += 1


def MergeSort(arr, copy_arr, left, right, cont = 0):
    if left < right:
        mid = left + (right - left) // 2
        if not (cont % 2):
            MergeSort(arr, copy_arr, left, mid, cont + 1)
            MergeSort(arr, copy_arr, mid + 1, right, cont + 1)
            Merge(arr, copy_arr, left, right)
        else:
            MergeSort(copy_arr, arr, left, mid, cont + 1)
            MergeSort(copy_arr, arr, mid + 1, right, cont + 1)
            Merge(copy_arr, arr, left, right)

def main():
    n = int(input('n = '))
    assert n >= 0
    if not n:
        return
    arr, copy_arr = [None for i in range(n)], []
    for idx in range(n):
        arr[idx] = int(input('arr[' + str(idx) + '] = '))
        copy_arr.append(arr[idx])
    print('Lista initiala: ' + str(arr))
    MergeSort(arr, copy_arr, 0, len(arr) - 1)
    print('Lista sortata/ordonata (crescator): ' + str(copy_arr))

main()