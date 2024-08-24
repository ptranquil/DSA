/** Using extra space */
function shiftZerostoEnd(nums) {
    let nonZero = [];
    let zeros = 0;
    for(let i=0;i<nums.length;i++){
        if(nums[i]!=0){
            nonZero.push(nums[i])
        } else {
            zeros++;
        }
    }
    console.log(zeros)
    while(zeros > 0){
        nonZero.push(0)
        zeros--
    }
    return nonZero
};

/** Modifying the same array */
function shiftZerostoEnd2(arr){
    let i=0
    while (i<arr.length-1){
        if(arr[i] == 0){
            j=i+1
            while(j<arr.length-1 && arr[j]==0){
                j++
            }
            [arr[i],arr[j]] = [arr [j],arr[i]]                
        }
        i++
    }
}
arr= [1,0,4,0,0,3,5,6,20,0]
console.log('After Shifting zeros : ',shiftZerostoEnd(arr))
shiftZerostoEnd2(arr)
console.log('After Shifting zeros with optimal approach: ',arr)