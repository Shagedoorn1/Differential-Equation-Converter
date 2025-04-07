package com.pyapp;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;

public class HomePanel extends JPanel {
    public HomePanel(CardLayout layout, JPanel container) {
        setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

        JLabel label = new JLabel("Choose A Panel: ");
        JButton button1 = new JButton("Load Control Systems");
        JButton button2 = new JButton("Load ODEs");

        button1.addActionListener((ActionEvent e) -> layout.show(container, "panel1"));
        button2.addActionListener((ActionEvent e) -> layout.show(container, "panel2"));

        add(label);
        add(Box.createRigidArea(new Dimension(0, 10)));
        add(button1);
        add(Box.createRigidArea(new Dimension(0, 10)));
        add(button2);
    }
}