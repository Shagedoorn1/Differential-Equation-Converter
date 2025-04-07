package com.pyapp;

import org.scilab.forge.jlatexmath.TeXFormula;
import org.scilab.forge.jlatexmath.TeXIcon;

import javax.swing.*;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.runtime.ExactConversionsSupport;

public class ControlPanel extends JPanel {

    public ControlPanel(CardLayout layout, JPanel container) {
        setLayout(new BorderLayout());

        JLabel label = new JLabel("Control Systems", SwingConstants.CENTER);
        JLabel outputLabel = new JLabel();

        JTextField inputField1 = new JTextField(5);
        JTextField inputField2 = new JTextField(5);
        JButton submitButton = new JButton("Submit");

        JButton backButton = new JButton("Back");
        backButton.addActionListener((ActionEvent e) -> layout.show(container, "home"));
        
        JPanel inputPanel = new JPanel();
        inputPanel.add(new JLabel("Input ODE:"));
        inputPanel.add(inputField1);
        inputPanel.add(new JLabel("Output ODE:"));
        inputPanel.add(inputField2);
        inputPanel.add(submitButton);

        submitButton.addActionListener((ActionEvent e) -> {
            String input1 = inputField1.getText();
            String input2 = inputField2.getText();

            try {
                ProcessBuilder pb = new ProcessBuilder("Python", "PyScripts/transfer.py", input1, input2);
                pb.redirectErrorStream(true);
                Process process = pb.start();

                BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                String output = reader.readLine();

                if (output != null && !output.isEmpty()) {
                    output = "{H\\left(s\\right) = " + output + "}";
                    TeXFormula formula = new TeXFormula(output);
                    TeXIcon icon = formula.createTeXIcon(TeXFormula.SERIF, 40);
                    outputLabel.setIcon(icon);
                    outputLabel.repaint();
                } else {
                    outputLabel.setText("No input recieved");
                }
            } catch (Exception ex) {
                ex.printStackTrace();
                outputLabel.setText("Error" + ex.getMessage());
            }
        });
        add(label, BorderLayout.NORTH);
        add(inputPanel, BorderLayout.WEST);
        add(outputLabel, BorderLayout.CENTER);
        add(backButton, BorderLayout.SOUTH);
    }
}