import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;



public class minimum_absolute_diference {
    static double minimo = Double.POSITIVE_INFINITY;

    public static void main(String[] args){
        int head;
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        try {
            int n = Integer.parseInt(bufferedReader.readLine());
            String[] arrTemp = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");
            List<Integer> arr = new ArrayList<>();

            for (int i = 0; i < n; i++) {
                int arrItem = Integer.parseInt(arrTemp[i]);
                arr.add(arrItem);
            }
            for (int i = 0; i < n-1; i++) {
                head = arr.remove(0);
                if (minimo_absoluto(head,arr)){
                    break;
                }
            }
            int min = (int) minimo;
            System.out.println(min);


        } catch (IOException e) {
            e.printStackTrace();
        }





    }

    private static Boolean minimo_absoluto(int n, List<Integer> array){
        for (int i = 0; i < array.size(); i++) {
            minimo = Math.min(minimo,Math.min(Math.abs(n-array.get(i)),Math.abs(array.get(i)-n)));
            if (minimo == 0){
                return true;
            }
        }
        return false;





    }
}
