package za.co.wethinkcode.mastermind;

import java.io.InputStream;
import java.util.Scanner;

public class Player {
    private final Scanner inputScanner;

    public Player(){
        this.inputScanner = new Scanner(System.in);
    }

    public Player(InputStream inputStream){
        this.inputScanner = new Scanner(inputStream);
    }

    /**
     * Gets a guess from user via text console.
     * This must prompt the user to re-enter a guess until a valid 4-digit string is entered, or until the user enters `exit` or `quit`.
     *
     * @return the value entered by the user
     */
    public String getGuess() {
// check for empty strings
        boolean validCode = false;
        char[] code = new char[4];

        System.out.println("Input 4 digit code:");
        String input;
        input = inputScanner.nextLine();

        while (validCode == false) {
            if (input.equals("exit") || input.equals("quit")) {
                break;
            }

            if (input.length() == 4) {
                for (int i = 0; i < input.length(); i++) {
                    code[i] = input.charAt(i);
                }
                for (int i = 0; i < input.length(); i++) {
                    if (Character.isDigit(code[i])) {
                        if (1 <= Integer.parseInt(String.valueOf(code[i])) &&
                                8 >= Integer.parseInt(String.valueOf(code[i]))) {
                            validCode = true;
                        } else {
                            validCode = false;
                            break;
                        }
                    } else {
                        validCode = false;
                        break;
                    }
                }
            } else if (input.isBlank()) {
                validCode = false;
            } else {
                validCode = false;
            }

//            if (input.isBlank()) {
//                validCode = false;
//            }

            if (!validCode) {
                System.out.println("Please enter exactly 4 digits (each from 1 to 8).");
                System.out.println("Input 4 digit code:");
                input = inputScanner.nextLine();
            }
        }
        return input;
    }
}

