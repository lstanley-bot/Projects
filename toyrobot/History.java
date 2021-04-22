package za.co.wethinkcode.toyrobot;

import java.util.ArrayList;
import java.util.List;

public class History {
    private List<String> commands;

    public History(){
        commands = new ArrayList<>();
    }

    public List<String> getCommands(){
        return this.commands;
    }

    public void append(Command command){
        switch(command.getName()){
            case "forward":
            case "back":
            case "sprint":
                this.commands.add(command.getName() + " " + command.getArgument());
                break;
            case "left":
            case "right":
                this.commands.add(command.getName());
                break;
        }
    }

    public void removeLast(){
        int i = this.commands.size() - 1;
        commands.remove(i);
    }
}
