package dr.lucas.batista.codigosjava;

import java.util.Scanner;

public class Beecrowd1001 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);  //Crio o recurso de leitura de variável

        int a, b;

        a = input.nextInt();
        b = input.nextInt();

        System.out.println("X = " + (a+b));

        input.close(); //encerro esse recurso
    }
}
