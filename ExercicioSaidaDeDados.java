package com.mycompany.codandoemjava;
import java.util.Locale;
public class ExercicioSaidaDeDados {
    public static void main(String[] args) {
        String product1Var = "Computer";
        String product2Var =  "Office Desk";

        int ageVar = 30;
        int codeVar = 5290;
        char genderVar = 'F';  // Aspas simples

        double price1Var = 2100.0;
        double price2Var = 650.50;
        double measureVar = 53.234567;

        System.out.println("Products:");
        System.out.printf("%s, Which price is $ %.2f\n", product1Var, price1Var);
        System.out.printf("%s, which price is $ %.2f\n", product2Var, price2Var);
        System.out.println(" ");
        System.out.printf("Record: %d years old, code %d and gender: %s\n", ageVar, codeVar, genderVar);  //qual é o marcador do char? --> Funcionou o %s
        System.out.println(" ");
        System.out.printf("Measure with eight decimal places: %.8f\n", measureVar);
        System.out.printf("Rounded (three decimal places): %.3f\n", measureVar);
        Locale.setDefault(Locale.US);
        System.out.printf("US decimal point: %.3f", measureVar);
    }
}
