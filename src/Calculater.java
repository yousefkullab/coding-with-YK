
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BorderFactory;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextField;

public class Calculater extends JFrame implements ActionListener

{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	Container c;
	JPanel p;
	JLabel firstNumber = new JLabel("First Number : ");
	JTextField t1 = new JTextField();
	JLabel secondNumber = new JLabel("Second Number : ");
	JTextField t2 = new JTextField();
	JLabel result = new JLabel("Result : ");
	JTextField t3 = new JTextField();
	JRadioButton r1 = new JRadioButton("Add");
	JRadioButton r2 = new JRadioButton("Sub");
	JRadioButton r3 = new JRadioButton("Div");
	JRadioButton r4 = new JRadioButton("Multi");
	JButton cal = new JButton("Calculator");
	ButtonGroup group;

	public Calculater() {
		super("Calcualtor");
		c = getContentPane();
		c.setLayout(null);

		firstNumber.setBounds(20, 20, 120, 30);
		t1.setBounds(120, 20, 170, 30);
		secondNumber.setBounds(20, 60, 120, 30);
		t2.setBounds(120, 60, 170, 30);
		result.setBounds(20, 100, 80, 30);
		t3.setBounds(120, 100, 170, 30);
		t3.setEditable(false);
		cal.setBounds(20, 200, 300, 40);
		cal.setFont(new Font("Dialog", Font.BOLD, 20));
		cal.addActionListener(this);

		p = new JPanel();
		p.setLayout(new FlowLayout());
		p.setBounds(20, 140, 300, 50);
		p.setBorder(BorderFactory.createTitledBorder("Operation"));
		group = new ButtonGroup();
		group.add(r1);
		group.add(r2);
		group.add(r3);
		group.add(r4);
		r1.addActionListener(this);
		r2.addActionListener(this);
		r3.addActionListener(this);
		r4.addActionListener(this);

		p.add(r1);
		p.add(r2);
		p.add(r3);
		p.add(r4);

		c.add(p);
		c.add(firstNumber);
		c.add(t1);
		c.add(secondNumber);
		c.add(t2);
		c.add(result);
		c.add(t3);
		c.add(cal);

		setSize(350, 300);
		setLocationRelativeTo(null);
		setResizable(false);
		setVisible(true);

	}

	@Override
	public void actionPerformed(ActionEvent e) {
		try {
			float x, y;
			if (r1.isSelected() && e.getSource() == cal) {
				x = Float.parseFloat(t1.getText());
				y = Float.parseFloat(t2.getText());
				t3.setText(Float.toString(x + y));
			} else if (r2.isSelected() && e.getSource() == cal) {
				x = Float.parseFloat(t1.getText());
				y = Float.parseFloat(t2.getText());
				t3.setText(Float.toString(x - y));
			} else if (r3.isSelected() && e.getSource() == cal) {
				x = Float.parseFloat(t1.getText());
				y = Float.parseFloat(t2.getText());
				t3.setText(Float.toString(x / y));
			} else if (r4.isSelected() && e.getSource() == cal) {
				x = Float.parseFloat(t1.getText());
				y = Float.parseFloat(t2.getText());
				t3.setText(Float.toString(x * y));
			}
		} catch (NumberFormatException ex) {
			JOptionPane.showMessageDialog(null, "Please Enter valid number");
		}
	}

	public static void main(String[] args) {
		new Calculater();
	}

}

// Software Engineer Joseph 