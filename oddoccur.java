/**
 * oddoccur
 */
public class oddoccur {
    public static void main(String[] args) {
        int[] data = { 9, 3, 9, 3, 9, 7, 9 };
        int jomblo = checkOddOccurences(data);
        System.out.println("element ke-" + jomblo + "(" + data[jomblo] + ") tidak mempunyai pasangan");
    }   
    
    public static int checkOddOccurences(int[] dataArray) {
        for (int i=0; i<dataArray.length; i++) {
            int num =0;
            for (int j=0; j<dataArray.length; j++){
                if (dataArray[i] == dataArray[j]) {
                    num++;
                }
            }
            if (num % 2 == 1){
                return i;
            }
        }
        return -1;
    } 
}