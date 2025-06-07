package persistencia;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

// Clase Empleado
class Empleado implements Serializable {
    String nombre;
    int edad;
    float salario;

    public Empleado(String nombre, int edad, float salario) {
        this.nombre = nombre;
        this.edad = edad;
        this.salario = salario;
    }

    public String toString() {
        return nombre + " - Edad: " + edad + ", Salario: " + salario;
    }
}

// Clase ArchivoEmpleado
class ArchivoEmpleado {
    // Atributo
    private String nomA;
    private List<Empleado> empleados = new ArrayList<>();

    // Constructor
    public ArchivoEmpleado(String n) { // Constructor
        this.nomA = n;
        crearArchivo(); // Cargar si existe
    }

    private void crearArchivo() {
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(nomA))) {
            empleados = (List<Empleado>) in.readObject();
        } catch (Exception e) {
            empleados = new ArrayList<>();
        }
    }

    // a)
    public void guardarEmpleado(Empleado e) {
        empleados.add(e);
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(nomA))) {
            out.writeObject(empleados);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    // b)
    public Empleado buscaEmpleado(String n) {
        for (Empleado e : empleados) {
            if (e.nombre.equalsIgnoreCase(n)) {
                return e;
            }
        }
        return null;
    }

    // c)
    public Empleado mayorSalario(float sueldo) {
        for (Empleado e : empleados) {
            if (e.salario > sueldo) {
                return e;
            }
        }
        return null;
    }
}

// Clase principal para pruebas
class Main {
    public static void main(String[] args) {
        ArchivoEmpleado archivo = new ArchivoEmpleado("empleados.dat");

        // a)
        archivo.guardarEmpleado(new Empleado("Ana", 30, 3000));
        archivo.guardarEmpleado(new Empleado("Luis", 40, 4500));

        // b)
        Empleado encontrado = archivo.buscaEmpleado("Ana");
        System.out.println("Encontrado: " + encontrado);

        // c)
        Empleado conMayorSalario = archivo.mayorSalario(3500);
        System.out.println("Mayor salario que 3500: " + conMayorSalario);
    }
}
