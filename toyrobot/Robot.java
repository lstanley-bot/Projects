package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.world.IWorld;

import java.util.ArrayList;
import java.util.List;

public class Robot {
    private History history;
    private String status;
    private final String name;
    private List<String> commandList = new ArrayList<>();
    private IWorld world;

    public static final Position CENTRE = new Position(0,0);

    public Robot(String name) {
        this.name = name;
        this.status = "Ready";
        this.history = new History();
    }


    public IWorld getWorld() {
        return world;
    }


    public History getHistory() {
        return history;
    }


    public void setWorld(IWorld world) {
        this.world = world;
    }


    public List<String> getCommandList() {
        return this.commandList;
    }


    public boolean handleCommand(Command command) {
        history.append(command);
        return command.execute(this);
    }


    @Override
    public String toString() {
        return "[" + this.getWorld().getPosition().getX() + "," + this.getWorld().getPosition().getY() + "] "
                + this.name + "> " + this.status;
    }


    public void setStatus(String status) {
        this.status = status;
    }


    public void addCommand(String command) {
        this.commandList.add(command);
    }


    public void setCommandList(List<String> commandList) {
        this.commandList = commandList;
    }


    public String getName() {
        return name;
    }

    public String getStatus() {
        return this.status;
    }
}