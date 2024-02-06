package dr.lucas.batista.codigosjava;

    import java.awt.Dimension;
import java.awt.Toolkit;

public class ResolucaoTela {
    public static void main(String[] args) {
        Dimension dimensao = Toolkit.getDefaultToolkit().getScreenSize();  //tools é uma variável que contém o método getDefaultToolkit()
        double largura = dimensao.getWidth();
        double altura = dimensao.getHeight();
        System.out.println("A resolução dessa tela é: ");
        System.out.println(largura + " x " + altura);
}
}

//dúvidas sobre a lógica dos métodos, atributos e etc. --> estudar
