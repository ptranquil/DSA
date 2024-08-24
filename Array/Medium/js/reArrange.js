/** Rearrange Array Elements by Sign without altering the relative order*/

arr = [-1, 4, 5, 1, 7, 8, 2, -2, -4, -5, -6, -43]
/** 
 * BruteForce 
 * The problem can be solved but here the relatove order can't be maintained
 * TC: O(N)
 * */
function reArrangeArr(arr) {
    pos = []
    neg = []
    for (let ele of arr) {
        if (ele > 0) {
            pos.push(ele)
        } else {
            neg.push(ele)
        }
    }
    temp = []
    for (let i = 0; i < pos.length; i++) {
        temp.push(pos[i])
        temp.push(neg[i])
    }
    console.log('Array after rearrange : ', temp)
}
reArrangeArr(arr)


/** 
 * two-pointer approach 
 * SC = TC = O(N)
*/
function reArrange2P(arr) {
    res = []
    posIndex = 0
    negIndex = 1
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            res[posIndex] = arr[i]
            posIndex += 2
        } else {
            res[negIndex] = arr[i]
            negIndex += 2
        }
    }
    console.log('Array after rearrange2PPP : ', res)
}

reArrange2P(arr)


/** 
 * Condition where the count is not equal
 * positive can be greater than negative or vice versa
 */

function RearrangebySign(A) {

    let n = A.length;

    // Define 2 arrays, one for storing positive 
    // and other for negative elements of the array.
    let pos = [];
    let neg = [];

    // Segregate the array into positives and negatives.
    for (let i = 0; i < n; i++) {

        if (A[i] > 0) pos.push(A[i]);
        else neg.push(A[i]);
    }

    // If positives are lesser than the negatives.
    if (pos.length < neg.length) {

        // First, fill array alternatively till the point 
        // where positives and negatives are equal in number.
        for (let i = 0; i < pos.length; i++) {

            A[2 * i] = pos[i];
            A[2 * i + 1] = neg[i];
        }

        // Fill the remaining negatives at the end of the array.
        let index = pos.length * 2;
        for (let i = pos.length; i < neg.length; i++) {

            A[index] = neg[i];
            index++;
        }
    }

    // If negatives are lesser than the positives.
    else {

        // First, fill array alternatively till the point 
        // where positives and negatives are equal in number.
        for (let i = 0; i < neg.length; i++) {

            A[2 * i] = pos[i];
            A[2 * i + 1] = neg[i];
        }

        // Fill the remaining positives at the end of the array.
        let index = neg.length * 2;
        for (let i = neg.length; i < pos.length; i++) {

            A[index] = pos[i];
            index++;
        }
    }
    // return A;
    console.log('The array : ',A)

}

// Array Initialisation.
let A = [1, 2, -4, -5, 3, 4];
RearrangebySign(A);