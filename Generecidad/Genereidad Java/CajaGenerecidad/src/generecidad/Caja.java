package generecidad;

public class Caja<T> {
    // a)
    private T contenido;

    public void guardar(T valor) {
        this.contenido = valor;
    }

    public T obtener() {
        return contenido;
    }

    public static void main(String[] args) {
        // b)
        Caja<Integer> cajaEntero = new Caja<>();
        cajaEntero.guardar(42);

        Caja<String> cajaTexto = new Caja<>();
        cajaTexto.guardar("Hola mundo");

        // c)
        System.out.println("Contenido de cajaEntero: " + cajaEntero.obtener());
        System.out.println("Contenido de cajaTexto: " + cajaTexto.obtener());
    }
}
