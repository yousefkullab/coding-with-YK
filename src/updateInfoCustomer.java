
import java.awt.Color;
import java.awt.Container;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPasswordField;
import javax.swing.JTextField;

public class updateInfoCustomer extends JFrame implements ActionListener {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	Container c;
	JButton close = new JButton("X");

	JLabel addNew = new JLabel("Update Info Customer");
	JButton add_btn = new JButton("Update Customer");
	JButton cancel = new JButton("Cancel");

	JLabel customerId = new JLabel("Customer ID : ");
	JTextField customerId_txt = new JTextField();
	JLabel customerName = new JLabel("Customer Name : ");
	JTextField customerName_txt = new JTextField();
	JLabel address = new JLabel("Address : ");
	JTextField address_txt = new JTextField();
	JLabel userName = new JLabel("User Name : ");
	JTextField userName_txt = new JTextField();
	JLabel password = new JLabel("Password : ");
	JPasswordField password_txt = new JPasswordField();

	public updateInfoCustomer() {
		c = getContentPane();
		getContentPane().setBackground(new Color(209, 232, 240));
		setLayout(null);
		customerId.setBounds(40, 120, 100, 30);
		customerId.setForeground(new Color(62, 119, 185));
		customerId_txt.setBounds(150, 120, 200, 30);
		customerName.setBounds(40, 180, 150, 30);
		customerName.setForeground(new Color(62, 119, 185));
		customerName_txt.setBounds(150, 180, 300, 30);
		address.setBounds(40, 240, 150, 30);
		address.setForeground(new Color(62, 119, 185));
		address_txt.setBounds(150, 240, 300, 30);
		userName.setBounds(40, 300, 150, 30);
		userName.setForeground(new Color(62, 119, 185));
		userName_txt.setBounds(150, 300, 200, 30);
		password.setBounds(40, 360, 150, 30);
		password.setForeground(new Color(62, 119, 185));
		password_txt.setBounds(150, 360, 200, 30);

		close.setBounds(550, 5, 45, 45);
		close.setForeground(new Color(62, 119, 185));
		close.setBackground(new Color(209, 232, 240));
		close.setBorder(null);
		close.setFocusPainted(false);
		close.addActionListener(this);
		addNew.setBounds(200, 40, 200, 30);
		addNew.setFont(new Font("Comic Sans MS", Font.BOLD, 17));

		add_btn.setBounds(70, 420, 200, 35);
		add_btn.addActionListener(this);
		cancel.setBounds(330, 420, 150, 35);
		cancel.addActionListener(this);

		c.add(customerId);
		c.add(customerId_txt);
		c.add(customerName);
		c.add(customerName_txt);
		c.add(address);
		c.add(address_txt);
		c.add(userName);
		c.add(userName_txt);
		c.add(password);
		c.add(password_txt);
		c.add(add_btn);
		c.add(cancel);
		c.add(addNew);
		c.add(close);

		setSize(600, 500);
		setUndecorated(true);
		setLocationRelativeTo(null);
		setVisible(true);
		setResizable(false);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

	}

	public static void main(String[] args) {
		new updateInfoCustomer();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == close)
			this.setVisible(false);
		if (e.getSource() == cancel)
			this.setVisible(false);
		if (e.getSource() == add_btn) {
			setVisible(false);
			JOptionPane.showMessageDialog(this, "Update Customer susscefly");

		}
	}

}
