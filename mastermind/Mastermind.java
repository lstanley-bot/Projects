package za.co.wethinkcode.mastermind;

public class Mastermind {
    private final String code;
    private final Player player;

    public Mastermind(CodeGenerator generator, Player player){
        this.code = generator.generateCode();
        this.player = player;
    }
    public Mastermind(){
        this(new CodeGenerator(), new Player());
    }

    public void runGame(){
        //TODO: implement the main run loop logic

        System.out.println("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.");

        String guess = player.getGuess();


        int tries = 12;

//        while(!(guess.equals("exit") || guess.equals("quit"))){
//            if (this.code.equals(guess)){
//                correctDigits += 1;
//            }else if(!(this.code.equals(guess))){
//                incorrectDigits += 1;
//            }
        while(!(guess.equals("exit") || guess.equals("quit"))){
            int correctDigits = 0;
            int incorrectDigits = 0;
            for(int i = 0; i < 4; i++){
                char a = this.code.charAt(i);

                if(guess.charAt(i) == this.code.charAt(i)){
                    correctDigits++;
                }else if(guess.contains(String.valueOf(a))){
                    incorrectDigits++;
                }
            }
        System.out.println("Number of correct digits in correct place: " + correctDigits);
        System.out.println("Number of correct digits not in correct place: " + incorrectDigits);

        if (tries == 1){
            System.out.println("No more turns left.");
            System.out.println("The code was: " + this.code);
            break;
        }else if(this.code.equals(guess)){
            System.out.println("Congratulations! You are a codebreaker!");
            System.out.println("The code was: " + this.code);
            break;
        }else if (!(guess.equals(this.code))){
            tries -= 1;
            System.out.println("Turns left: " + tries);
        }
//        System.out.println("Turns left: " + tries);
        guess = player.getGuess();
        }
    }

    public static void main(String[] args){
        Mastermind game = new Mastermind();
        game.runGame();
//        CodeGenerator code = new CodeGenerator();
//        code.generateCode();
//        Player player = new Player();
//        player.getGuess();
    }
}
