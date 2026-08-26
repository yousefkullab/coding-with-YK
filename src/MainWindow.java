import java.awt.Color;
import java.awt.Container;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class MainWindow extends JFrame implements ActionListener {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	Container c;
	JPanel up_pnl = new JPanel();
	JLabel logo_label = new JLabel();
	JLabel l1 = new JLabel("Welcome to our library");
	JLabel l2 = new JLabel("we are happy when join us ^_^");
	JButton close_btn;

	JPanel down_pal = new JPanel();
	JLabel main_img_label = new JLabel();
	ImageIcon main_img, manager_Img, customer_Img;
	JLabel manager_label = new JLabel();
	JLabel customer_label = new JLabel();
	JButton manager_btn, customers_btn;

	public MainWindow() {

		c = getContentPane();
		setLayout(null);

		up_pnl.setLayout(null);
		up_pnl.setBounds(0, 0, 950, 150);
		up_pnl.setBackground(new Color(62, 119, 185));

		logo_label.setIcon(new ImageIcon("logo.png"));
		logo_label.setBounds(20, 5, 200, 150);
		l1.setBounds(210, 10, 500, 100);
		l1.setFont(new Font("Comic Sans MS", Font.BOLD, 35));
		l1.setForeground(Color.white);
		l2.setBounds(210, 50, 300, 100);
		l2.setFont(new Font("Comic Sans MS", Font.ITALIC, 15));
		l2.setForeground(Color.white);

		close_btn = new JButton("X");
		close_btn.setBounds(900, 5, 45, 45);
		close_btn.setBackground(new Color(62, 119, 185));
		close_btn.setForeground(Color.white);
		close_btn.setBorder(null);
		close_btn.setFocusPainted(false);
		close_btn.addActionListener(this);

		up_pnl.add(logo_label);
		up_pnl.add(l1);
		up_pnl.add(l2);
		up_pnl.add(close_btn);

		down_pal.setLayout(null);
		down_pal.setBounds(0, 150, 950, 450);

		main_img = new ImageIcon("main_img.png");
		main_img_label.setIcon(main_img);
		main_img_label.setBounds(0, 0, 950, 450);

		manager_label.setBorder(BorderFactory.createLineBorder(new Color(62, 119, 185), 1));
		manager_label.setBounds(70, 50, 120, 130);
		manager_Img = new ImageIcon("manager.png");
		manager_label.setIcon(manager_Img);
		manager_btn = new JButton("Manager");
		manager_btn.setBackground(Color.white);
		manager_btn.setFont(new Font("Comic Sans MS", Font.BOLD, 17));
		manager_btn.setForeground(new Color(62, 119, 185));
		manager_btn.setBorder(null);
		manager_btn.setBounds(5, 95, 100, 30);
		manager_label.add(manager_btn);
		manager_btn.addActionListener(this);
		main_img_label.add(manager_label);

		customer_label.setBorder(BorderFactory.createLineBorder(new Color(62, 119, 185), 1));
		customer_label.setBounds(70, 200, 120, 130);
		customer_Img = new ImageIcon("clients.png");
		customer_label.setIcon(customer_Img);
		customers_btn = new JButton("Customers");
		customers_btn.setBackground(Color.white);
		customers_btn.setFont(new Font("Comic Sans MS", Font.BOLD, 17));
		customers_btn.setForeground(new Color(62, 119, 185));
		customers_btn.setBorder(null);
		customers_btn.setBounds(5, 95, 100, 30);
		customer_label.add(customers_btn);
		customers_btn.addActionListener(this);
		main_img_label.add(customer_label);

		down_pal.add(main_img_label);

		c.add(up_pnl);
		c.add(down_pal);

		setSize(950, 600);
		setUndecorated(true);
		setLocationRelativeTo(null);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	public static void main(String[] args) {
		new MainWindow();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == close_btn)
			System.exit(0);
		if (e.getSource() == manager_btn)
			new ManagerLogin();
	}

}
// Software Engineer Jsoeph . 20202273
