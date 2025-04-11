function binarySearch(arr, low, high, ele) {
    if (low > high) return -1
    let mid = Math.floor((low + high) / 2)
    if (arr[mid] < ele) {
        return binarySearch(arr, mid + 1, high, ele)
    } else if (arr[mid] > ele) {
        return binarySearch(arr, low, mid - 1, ele)
    } else {
        return mid
    }
}

let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
let N = arr.length;
console.log(binarySearch(arr, 0, N, 11))  