package persistencia;
import java.io.*;
import java.util.*;

// a) Clase Cliente
class Cliente implements Serializable {
    int id;
    String nombre;
    int telefono;

    public Cliente(int id, String nombre, int telefono) {
        this.id = id;
        this.nombre = nombre;
        this.telefono = telefono;
    }

    public String toString() {
        return "ID: " + id + ", Nombre: " + nombre + ", Teléfono: " + telefono;
    }
}

// a) Clase ArchivoCliente
class ArchivoCliente {
    private String nomA;

    public ArchivoCliente(String nomA) {
        this.nomA = nomA;
    }

    private List<Cliente> leerArchivo() {
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(nomA))) {
            return (List<Cliente>) in.readObject();
        } catch (Exception e) {
            return new ArrayList<>();
        }
    }

    private void escribirArchivo(List<Cliente> clientes) {
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(nomA))) {
            out.writeObject(clientes);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // a) guardar cliente
    public void guardaCliente(Cliente c) {
        List<Cliente> clientes = leerArchivo();
        clientes.add(c);
        escribirArchivo(clientes);
    }

    // b) buscar por ID
    public Cliente buscarCliente(int id) {
        for (Cliente c : leerArchivo()) {
            if (c.id == id) return c;
        }
        return null;
    }

    // c) buscar por ID y mostrar teléfono
    public String buscarCelularCliente(int id) {
        for (Cliente c : leerArchivo()) {
            if (c.id == id) {
                return c.nombre + " - Teléfono: " + c.telefono;
            }
        }
        return "Cliente no encontrado";
    }
}

// Clase principal
public class Main {
    public static void main(String[] args) {
        ArchivoCliente archivo = new ArchivoCliente("clientes.dat");

        // a)
        archivo.guardaCliente(new Cliente(1, "Mario", 123456));
        archivo.guardaCliente(new Cliente(2, "Laura", 987654));

        // b)
        Cliente buscado = archivo.buscarCliente(1);
        System.out.println("Cliente encontrado: " + buscado);

        // c)
        String celular = archivo.buscarCelularCliente(2);
        System.out.println("Datos + Teléfono: " + celular);
    }
}
