package za.co.wethinkcode.fizzbuzz;

import java.util.Arrays;

public class FizzBuzz {
    public String checkNumber(int number) {
        boolean divisibleBy3 = number % 3 == 0;
        boolean divisibleBy5 = number % 5 == 0;

        if ( divisibleBy3 && !divisibleBy5 ) {
            return "Fizz";
        }
        if ( !divisibleBy3 && divisibleBy5 ) {
            return "Buzz";
        }
        if ( divisibleBy3 && divisibleBy5 ) {
            return "FizzBuzz";
        }
        return String.valueOf(number);
    }

    public String countTo(int number) {
        za.co.wethinkcode.fizzbuzz.FizzBuzz fizzBuzz = new FizzBuzz();
        String answer[] = new String[number+1];
        for (int i = 0; i < number+1; i++){
            answer[i] = fizzBuzz.checkNumber(i);
        }

        int n = answer.length-1;
        String[] finalAnswer = new String[n];
        System.arraycopy(answer,1,finalAnswer,0,n);

        return Arrays.toString(finalAnswer);
    }
}
