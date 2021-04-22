package za.co.wethinkcode.mastermind;

import java.util.Random;

public class CodeGenerator {
    private final Random random;

    public CodeGenerator(){
        this.random = new Random();
    }

    public CodeGenerator(Random random){
        this.random = random;
    }

    /**
     * Generates a random 4 digit code, using this.random, where each digit is in the range 1 to 8 only.
     * Duplicated digits are allowed.
     * @return the generated 4-digit code
     */
    public String generateCode(){
        //TODO: implement using this.random
        int a = 1 + random.nextInt(8);
        int b = 1 + random.nextInt(8);
        int c = 1 + random.nextInt(8);
        int d = 1 + random.nextInt(8);

        String code = Integer.toString(a) + Integer.toString(b) + Integer.toString(c) + Integer.toString(d);
//        System.out.println(code);
        return code;
    }
}
