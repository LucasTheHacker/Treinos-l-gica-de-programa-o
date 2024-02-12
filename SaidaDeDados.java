package com.mycompany.codandoemjava;

import java.util.Locale;  //Importa a classe Locale

public class SaidaDeDados {
    public static void main(String[] args) {  //Método main dentro da classe SaidaDeDados
        
        Locale.setDefault(Locale.US); //Com o idioma em inglês, o separador decimal vai ser o ponto.

        double y = 32.05;

        int anosVar = 19;

        String nomeVar = "Lucas";

        double rendaVar = 10.35784;  

        System.out.println(nomeVar);  //imprime o double

        System.out.printf("%.2f\n", rendaVar);  // 'printf(Formato, Variável)--> (2 casas decimais e quebra de linha, x)
                        // tanto o \n quanto o %n são quebras de linha
        System.out.printf("%.3f%n", rendaVar);  // 3 casas decimais + quebra de linha ao imprimir x

        System.out.printf("Resultado = %.2f metros\n", rendaVar); 
        //No local onde eu defino o formato da variável, ela é substituída. 

        System.out.printf("Resultados = %f, %f pontos\n", rendaVar, y);
        //Concatenação com FORMAT

        System.out.println(y);

        System.out.printf("%s tem %d anos de idade e ganha %.2f reais de dinheiros ", nomeVar, anosVar, rendaVar);
    }
} // FIM CLASSE SaidaDeDados 
