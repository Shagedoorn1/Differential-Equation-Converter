package com.pyapp;

import javax.swing.*;
import java.awt.*;
public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("PySysControl");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 400);
        
        CardLayout cardLayout = new CardLayout();
        JPanel mainPanel = new JPanel(cardLayout);
        HomePanel home = new HomePanel(cardLayout, mainPanel);
        ControlPanel panel1 = new ControlPanel(cardLayout, mainPanel);
        ODEPanel panel2 = new ODEPanel(cardLayout, mainPanel);

        mainPanel.add(home, "home");
        mainPanel.add(panel1, "panel1");
        mainPanel.add(panel2, "panel2");

        frame.setContentPane(mainPanel);
        frame.setVisible(true);
    }
}