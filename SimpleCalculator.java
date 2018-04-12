import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SimpleCalculator {

    public static void main(String[] args) throws IOException {
        System.out.println("This is a simple calculator!");
        System.out.print("Please enter the first number: ");
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        double n1 = Integer.parseInt(input.readLine());
        System.out.print("Please enter the operator: ");
        String operator = input.readLine();
        System.out.print("Please enter the second number: ");
        double n2 = Integer.parseInt(input.readLine());
        double result = 0;
        if(operator.equals("+")){
            result = n1 + n2;
        }
        else if(operator.equals("-")){
            result = n1 - n2;
        }
        else if(operator.equals("*")) {
            result = n1 * n2;
        }
        else if(operator.equals("/")) {
            result = n1 / n2;
        }
        else {
            System.err.println("Unknown Operator!");
            return;
        }
        System.out.println("The result is: " + result);
    }
}