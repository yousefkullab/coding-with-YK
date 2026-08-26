import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class MetricConverter extends JFrame implements ActionListener {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	Container c;
	JPanel input_pnl, key_pnl, control_pnl, choose_pnl;
	JLabel inputDistance = new JLabel("Distance in miles");
	JTextField inputDistance_txt = new JTextField(15);
	JButton btn[] = new JButton[12];
	JButton convert = new JButton("Convert");
	String s[] = { "1", "2", "3", "4", "5", "6", "7", "8", "9", "C", "0", "." };
	JTextArea txt_area = new JTextArea();
	JLabel from = new JLabel("From : ");
	JLabel to = new JLabel("to : ");
	JRadioButton fmm = new JRadioButton("mm");
	JRadioButton fcm = new JRadioButton("cm");
	JRadioButton fkm = new JRadioButton("km");
	JRadioButton tmm = new JRadioButton("mm");
	JRadioButton tcm = new JRadioButton("cm");
	JRadioButton tkm = new JRadioButton("km");
	ButtonGroup group1, group2;

	public MetricConverter() {
		super("Metric Converter");

		c = getContentPane();
		c.setLayout(new BorderLayout());
		input_pnl = new JPanel();
		input_pnl.add(inputDistance);
		input_pnl.add(inputDistance_txt);
		inputDistance_txt.setEditable(false);

		key_pnl = new JPanel();
		key_pnl.setLayout(new GridLayout(4, 4, 2, 2));

		for (int i = 0; i < btn.length; i++) {
			btn[i] = new JButton(s[i]);
			btn[i].addActionListener(this);
			key_pnl.add(btn[i]);
		}

		convert.addActionListener(this);

		control_pnl = new JPanel();
		control_pnl.setLayout(new BorderLayout());
		control_pnl.add(key_pnl, BorderLayout.EAST);
		control_pnl.add(convert, BorderLayout.SOUTH);

		choose_pnl = new JPanel();
		choose_pnl.setLayout(new GridLayout(4, 2, 8, 2));
		choose_pnl.add(from);
		choose_pnl.add(to);
		choose_pnl.add(fmm);
		choose_pnl.add(tmm);
		choose_pnl.add(fcm);
		choose_pnl.add(tcm);
		choose_pnl.add(fkm);
		choose_pnl.add(tkm);
		txt_area.setEditable(false);

		group1 = new ButtonGroup();
		group1.add(fmm);
		group1.add(fcm);
		group1.add(fkm);

		group2 = new ButtonGroup();
		group2.add(tmm);
		group2.add(tcm);
		group2.add(tkm);

		fmm.addActionListener(this);
		fcm.addActionListener(this);
		fkm.addActionListener(this);

		c.add(input_pnl, BorderLayout.NORTH);
		c.add(control_pnl, BorderLayout.EAST);
		c.add(txt_area, BorderLayout.CENTER);
		c.add(choose_pnl, BorderLayout.WEST);

		setSize(500, 250);
		setResizable(false);
		setLocationRelativeTo(null);
		setVisible(true);

	}

	public static void main(String[] args) {
		new MetricConverter();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		try {
			if (fmm.isSelected()) {
				tmm.setSelected(false);
				tmm.setEnabled(false);
				tcm.setEnabled(true);
				tkm.setEnabled(true);

			} else if (fcm.isSelected()) {
				tcm.setSelected(false);
				tcm.setEnabled(false);
				tmm.setEnabled(true);
				tkm.setEnabled(true);
			} else {
				tkm.setSelected(false);
				tkm.setEnabled(false);
				tmm.setEnabled(true);
				tcm.setEnabled(true);

			}

			String command = e.getActionCommand();
			switch (command) {
			case "0":
			case "1":
			case "2":
			case "3":
			case "4":
			case "5":
			case "6":
			case "7":
			case "8":
			case "9":
				inputDistance_txt.setText(inputDistance_txt.getText() + command);
				break;
			case "C":
				inputDistance_txt.setText("");
				break;
			case ".":
				if (inputDistance_txt.getText().indexOf(".") == -1)
					inputDistance_txt.setText(inputDistance_txt.getText() + command);
				break;

			case "Convert":
				String s = inputDistance_txt.getText();
				double x = Double.parseDouble(s);
				if (fmm.isSelected() && tcm.isSelected()) {
					double x1 = x / 10;
					txt_area.append("The distance " + x + " mm = " + x1 + " cm\n");
				}
				if (fmm.isSelected() && tkm.isSelected()) {
					double x2 = x * 0.000001;
					txt_area.append("The distance " + x + " mm = " + x2 + " km\n");
				}
				if (fcm.isSelected() && tmm.isSelected()) {
					double x3 = x * 10;
					txt_area.append("The distance " + x + " cm = " + x3 + " mm\n");
				}
				if (fcm.isSelected() && tkm.isSelected()) {
					double x4 = x / 100000;
					txt_area.append("The distance " + x + " cm = " + x4 + " km\n");
				}
				if (fkm.isSelected() && tmm.isSelected()) {
					double x5 = x * 1000000;
					txt_area.append("The distance " + x + " km = " + x5 + " mm\n");
				}
				if (fkm.isSelected() && tcm.isSelected()) {
					double x6 = x * 100000;
					txt_area.append("The distance " + x + " km = " + x6 + " cm\n");
				}

			}
		} catch (java.lang.NumberFormatException ex) {
			JOptionPane.showMessageDialog(this, "Please enter the value that want to convert it ??? ");
		}

	}

}
