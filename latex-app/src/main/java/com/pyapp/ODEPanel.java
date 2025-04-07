package com.pyapp;

import org.scilab.forge.jlatexmath.TeXFormula;
import org.scilab.forge.jlatexmath.TeXIcon;

import javax.swing.*;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class ODEPanel extends JPanel {
    public ODEPanel(CardLayout layout, JPanel container) {
        
        setLayout(new BorderLayout());
        
        JLabel label = new JLabel("ODEs", SwingConstants.CENTER);
        JLabel outputLabel = new JLabel();

        JTextField inputField = new JTextField(5);
        JButton submitButton = new JButton("submit");

        JButton backButton = new JButton("Back");
        backButton.addActionListener((ActionEvent e) -> layout.show(container, "home"));

        JPanel inputPanel = new JPanel();
        inputPanel.add(new JLabel("Input ODE:"));
        inputPanel.add(inputField);
        inputPanel.add(submitButton);

        submitButton.addActionListener((ActionEvent e) -> {
            String input = inputField.getText();

            try {
                ProcessBuilder pb = new ProcessBuilder("python", "PyScripts/translate.py", input);
                pb.redirectErrorStream(true);
                Process process = pb.start();

                BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                String output = reader.readLine();

                if (output != null && !output.isEmpty()) {
                    output = "{" + output + " = 0 }";
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