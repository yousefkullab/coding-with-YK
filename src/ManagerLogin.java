
import java.awt.Color;
import java.awt.Container;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;

public class ManagerLogin extends JFrame implements ActionListener {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	Container c;
	JLabel m = new JLabel("Manager Login");
	JPanel pnl = new JPanel();
	JLabel name = new JLabel("User Name: ");
	JTextField name_txt = new JTextField();
	JLabel password = new JLabel("Password: ");
	JPasswordField password_txt = new JPasswordField();
	JButton login = new JButton("Login");
	JButton cancel = new JButton("Cancel");
	JButton close = new JButton("X");
	JLabel close_btnLabel = new JLabel("x");

	public ManagerLogin() {
		c = getContentPane();
		c.setLayout(null);

		pnl.setLayout(null);
		pnl.setBackground(new Color(62, 119, 185));
		pnl.setBounds(0, 0, 500, 400);

		close_btnLabel.setBounds(450, 5, 45, 45);
		close_btnLabel.add(close);
		close.setBounds(450, 5, 45, 45);
		close.setBackground(new Color(62, 119, 185));
		close.setForeground(Color.white);
		close.setBorder(null);
		close.setFocusPainted(false);
		close.addActionListener(this);
		m.setFont(new Font("Comic Sans MS", Font.BOLD, 25));
		m.setForeground(Color.white);
		m.setBounds(150, 40, 250, 80);
		name.setBounds(30, 130, 100, 40);
		name.setForeground(Color.white);
		name.setFont(new Font("Comic Sans MS", Font.BOLD, 13));
		name_txt.setBounds(140, 130, 250, 40);
		password.setBounds(30, 200, 100, 40);
		password_txt.setBounds(140, 200, 250, 40);
		password.setForeground(Color.white);
		password.setFont(new Font("Comic Sans MS", Font.BOLD, 13));
		login.setBounds(100, 300, 120, 30);
		login.addActionListener(this);
		cancel.setBounds(280, 300, 120, 30);
		cancel.addActionListener(this);

		pnl.add(m);
		pnl.add(name);
		pnl.add(name_txt);
		pnl.add(password);
		pnl.add(password_txt);
		pnl.add(close_btnLabel);
		pnl.add(close);
		pnl.add(login);
		pnl.add(cancel);

		c.add(pnl);

		setSize(500, 400);
		setUndecorated(true);
		setLocationRelativeTo(null);
		setVisible(true);
		setResizable(false);
		setLocationRelativeTo(null);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

	}

	public static void main(String[] args) {
		new ManagerLogin();
	}

	@SuppressWarnings("deprecation")

	@Override
	public void actionPerformed(ActionEvent e) {

		String s = "123";
		if (e.getSource() == close || e.getSource() == cancel)
			this.setVisible(false);
		else if ((e.getSource() == login && name_txt.getText().equals(s))
				&& (e.getSource() == login && password_txt.getText().equals(s))) {
			new ManagerWindow();
			this.setVisible(false);

		} else {
			JOptionPane.showMessageDialog(this, "User Name is 123 \n Password is 123");
		}

	}

}
