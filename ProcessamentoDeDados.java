package dr.lucas.batista.codigosjava;

public class ProcessamentoDeDados {
    public static void main(String[] args) {
        double b, B, h, area;

        b = 6.0; //Boas práticas: ainda que seja um número redondo, usar o .0 por se tratar de um double.
        B = 8.0; //Boas práticas: se fosse um valor float, ficaria B = 8f;
        h = 5.0;

        area = (B + b) * h/2;

        System.out.println(area);

        int x, y;
        double resultado;

        x = 5;
        y = 2;
        resultado = x / y;
        System.out.println(resultado); // O programa imprime o 2, por entender que a divisão de dois ints resulta também em int. (Corta a parte flutuante)

        resultado = (double) x/y;  //Casting = Conversão explícita dos valores
        System.out.println(resultado); //Agora imprime o double 2.5

        double disney = 8.0;
        float euem = 8f;

        System.out.println(disney + " " + euem);
    }
    
}
