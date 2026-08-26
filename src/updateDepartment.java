import java.awt.Color;
import java.awt.Container;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class updateDepartment extends JFrame implements ActionListener {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	Container c;
	JButton close = new JButton("X");

	JLabel addNew = new JLabel("Update Department");
	JLabel name = new JLabel("Name : ");
	JTextField name_txt = new JTextField();
	JLabel description = new JLabel("Description : ");
	JTextArea txtArea = new JTextArea();
	JButton add_btn = new JButton("Update Department");
	JButton cancel = new JButton("Cancel");

	public updateDepartment() {
		c = getContentPane();
		setLayout(null);
		getContentPane().setBackground(new Color(209, 232, 240));
		close.setBounds(550, 5, 45, 45);
		close.setForeground(Color.black);
		close.setBackground(new Color(209, 232, 240));
		close.setBorder(null);
		close.setFocusPainted(false);
		close.addActionListener(this);
		addNew.setBounds(200, 40, 200, 30);
		addNew.setFont(new Font("Comic Sans MS", Font.BOLD, 17));
		name.setBounds(80, 100, 100, 30);
		name.setForeground(new Color(62, 119, 185));
		name_txt.setBounds(140, 100, 300, 30);
		description.setBounds(50, 170, 100, 30);
		description.setForeground(new Color(62, 119, 185));
		txtArea.setBounds(50, 210, 300, 200);
		add_btn.setBounds(70, 450, 200, 30);
		add_btn.addActionListener(this);
		cancel.setBounds(330, 450, 150, 30);

		c.add(name);
		c.add(name_txt);
		c.add(description);
		c.add(txtArea);
		c.add(add_btn);
		c.add(cancel);
		c.add(addNew);
		c.add(close);
		cancel.addActionListener(this);

		setSize(600, 500);
		setUndecorated(true);
		setLocationRelativeTo(null);
		setVisible(true);
		setResizable(false);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

	}

	public static void main(String[] args) {
		new updateDepartment();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == close)
			this.setVisible(false);
		if (e.getSource() == cancel)
			this.setVisible(false);
		if (e.getSource() == add_btn) {
			setVisible(false);
			JOptionPane.showMessageDialog(this, "Update Department susscefly");
		}
	}

}
