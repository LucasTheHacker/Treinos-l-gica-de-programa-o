package dr.lucas.batista.codigosjava;

import java.util.Date; //Importei uma biblioteca
 
public class HoraDoSistema {
    public static void main(String[] args) {
        Date relogio = new Date(); //o "new" cria um objeto e por meio do = eu associo esse objeto à variável relogio 
        System.out.println("A hora do sistema é:");
        System.out.println(relogio.toString()); //método toString
    }
}

//Date é uma classe com construtores e métodos
