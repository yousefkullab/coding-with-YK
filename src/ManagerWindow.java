import java.awt.Color;
import java.awt.Container;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTabbedPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class ManagerWindow extends JFrame implements ActionListener, MouseListener {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	Container c;
	JTabbedPane t = new JTabbedPane();
	JButton close = new JButton("X");
	JLabel img = new JLabel();
	JLabel title = new JLabel("Manager Window");

	JPanel dep_pnl = new JPanel();
	JLabel depList_l = new JLabel("Department List");
	JList<Object> dep_list = new JList<Object>();
	JLabel dep_name = new JLabel("Department Name :");
	JTextField dep_name_txt = new JTextField();
	JLabel dep_desctipetion = new JLabel("Description :");
	JTextArea dep_txtArea = new JTextArea();
	JButton dep_btn = new JButton("Add new Department");

	JPanel books_pnl = new JPanel();
	JLabel booksList_l = new JLabel("Books List");
	JList<Object> book_list = new JList<Object>();
	JLabel bookName = new JLabel("Book Name :");
	JTextField bookName_txt = new JTextField();
	JLabel price = new JLabel("Price :");
	JTextField price_txt = new JTextField();
	JLabel depBox = new JLabel("Department :");
	JComboBox<Object> dep_box = new JComboBox<Object>();
	JLabel copies = new JLabel("No.Copies :");
	JTextField copies_txt = new JTextField();
	JLabel author = new JLabel("Author :");
	JTextField author_txt = new JTextField();
	JLabel isbn = new JLabel("ISBN :");
	JTextField isbn_txt = new JTextField();
	JButton book_btn = new JButton("New Book");

	JPanel customer_pnl = new JPanel();
	JLabel custumerList = new JLabel("Customer List");
	JList<Object> custmer_list = new JList<Object>();
	JLabel customerId = new JLabel("Customer ID :");
	JTextField customerId_txt = new JTextField();
	JLabel customerName = new JLabel("Customer Name :");
	JTextField customerName_txt = new JTextField();
	JLabel address = new JLabel("Address :");
	JTextField address_txt = new JTextField();
	JLabel userName = new JLabel("User Name :");
	JTextField userName_txt = new JTextField();
	JLabel password = new JLabel("Password :");
	JPasswordField password_txt = new JPasswordField();
	JButton customer_btn = new JButton("New Customer");

	public ManagerWindow() {
		super("Manager Window");
		getContentPane().setBackground(new Color(209, 232, 240));
		c = getContentPane();
		c.setLayout(null);
		t.setBounds(40, 100, 770, 470);
		close.setBounds(800, 5, 45, 45);
		close.setForeground(new Color(5, 5, 78));
		close.setBackground(new Color(209, 232, 240));
		close.setBorder(null);
		close.setFocusPainted(false);
		close.addActionListener(this);
		img.setIcon(new ImageIcon("logo100.png"));
		img.setBounds(5, 5, 100, 100);
		title.setBounds(110, 20, 150, 50);
		title.setFont(new Font("Comic Sans MS", Font.BOLD, 15));
		//////////////////////////////////////////

		dep_pnl = new JPanel(null);
		dep_pnl.setBackground(new Color(62, 119, 185));
		depList_l.setBounds(15, 20, 100, 50);
		depList_l.setForeground(Color.white);
		dep_list.setBounds(15, 60, 200, 300);
		dep_list.addMouseListener(this);
		dep_name.setBounds(250, 70, 150, 30);
		dep_name.setForeground(Color.white);
		dep_name_txt.setBounds(400, 70, 300, 30);
		dep_name_txt.setEditable(false);
		dep_desctipetion.setBounds(250, 150, 100, 30);
		dep_desctipetion.setForeground(Color.white);
		dep_txtArea.setBounds(400, 150, 300, 200);
		dep_txtArea.setEditable(false);
		dep_btn.setBounds(270, 385, 200, 30);
		dep_btn.addActionListener(this);

		dep_pnl.add(depList_l);
		dep_pnl.add(dep_list);
		dep_pnl.add(dep_name);
		dep_pnl.add(dep_name_txt);
		dep_pnl.add(dep_desctipetion);
		dep_pnl.add(dep_txtArea);
		dep_pnl.add(dep_btn);

		//////////////////////////////////////////

		books_pnl = new JPanel(null);
		books_pnl.setBackground(new Color(62, 119, 185));
		booksList_l.setBounds(10, 10, 100, 40);
		booksList_l.setForeground(Color.white);
		book_list.setBounds(10, 60, 300, 300);
		book_list.addMouseListener(this);
		bookName.setBounds(400, 15, 100, 30);
		bookName.setForeground(Color.white);
		bookName_txt.setBounds(500, 15, 200, 30);
		bookName_txt.setEditable(false);
		price.setBounds(400, 60, 100, 30);
		price.setForeground(Color.white);
		price_txt.setBounds(500, 60, 100, 30);
		price_txt.setEditable(false);
		copies.setBounds(400, 110, 100, 30);
		copies.setForeground(Color.white);
		copies_txt.setBounds(500, 110, 100, 30);
		copies_txt.setEditable(false);
		depBox.setBounds(400, 160, 100, 30);
		depBox.setForeground(Color.white);
		dep_box.setBounds(500, 160, 150, 30);
		dep_box.setEditable(false);
		author.setBounds(400, 210, 100, 30);
		author.setForeground(Color.white);
		author_txt.setBounds(500, 210, 200, 30);
		author_txt.setEditable(false);
		isbn.setBounds(400, 260, 100, 30);
		isbn.setForeground(Color.white);
		isbn_txt.setBounds(500, 260, 200, 30);
		isbn_txt.setEditable(false);
		book_btn.setBounds(350, 380, 150, 30);
		book_btn.addActionListener(this);

		books_pnl.add(booksList_l);
		books_pnl.add(book_list);
		books_pnl.add(bookName);
		books_pnl.add(bookName_txt);
		books_pnl.add(price);
		books_pnl.add(price_txt);
		books_pnl.add(copies);
		books_pnl.add(copies_txt);
		books_pnl.add(depBox);
		books_pnl.add(dep_box);
		books_pnl.add(author);
		books_pnl.add(author_txt);
		books_pnl.add(isbn);
		books_pnl.add(isbn_txt);
		books_pnl.add(book_btn);

		/////////////////////////////////////////

		customer_pnl = new JPanel(null);
		customer_pnl.setBackground(new Color(62, 119, 185));
		custumerList.setBounds(15, 20, 100, 30);
		custumerList.setForeground(Color.white);
		custmer_list.setBounds(15, 50, 250, 300);
		custmer_list.addMouseListener(this);
		customerId.setBounds(350, 60, 100, 30);
		customerId.setForeground(Color.white);
		customerId_txt.setBounds(470, 60, 200, 30);
		customerId_txt.setEditable(false);
		customerName.setBounds(350, 110, 100, 30);
		customerName.setForeground(Color.white);
		customerName_txt.setBounds(470, 110, 270, 30);
		customerName_txt.setEditable(false);
		address.setBounds(350, 160, 100, 30);
		address.setForeground(Color.white);
		address_txt.setBounds(470, 160, 270, 30);
		address_txt.setEditable(false);
		userName.setBounds(350, 210, 100, 30);
		userName.setForeground(Color.white);
		userName_txt.setBounds(470, 210, 200, 30);
		userName_txt.setEditable(false);
		password.setBounds(350, 260, 100, 30);
		password.setForeground(Color.white);
		password_txt.setBounds(470, 260, 200, 30);
		password_txt.setEditable(false);
		customer_btn.setBounds(330, 370, 150, 30);
		customer_btn.addActionListener(this);

		customer_pnl.add(custumerList);
		customer_pnl.add(custmer_list);
		customer_pnl.add(customerId);
		customer_pnl.add(customerId_txt);
		customer_pnl.add(customerName);
		customer_pnl.add(customerName_txt);
		customer_pnl.add(address);
		customer_pnl.add(address_txt);
		customer_pnl.add(userName);
		customer_pnl.add(userName_txt);
		customer_pnl.add(password);
		customer_pnl.add(password_txt);
		customer_pnl.add(customer_btn);

		/////////////////////////////////////////
		t.add("Department", dep_pnl);
		t.add("Books", books_pnl);
		t.add("Customer", customer_pnl);
		c.add(close);
		c.add(img);
		c.add(title);
		c.add(t);

		setSize(850, 600);
		setUndecorated(true);
		setVisible(true);
		setResizable(false);
		setLocationRelativeTo(null);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

	}

	public static void main(String[] args) {
		new ManagerWindow();
	}

	@Override
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mousePressed(MouseEvent e) {
		if (e.getSource() == dep_list) {
			if (e.getClickCount() == 2)
				new updateDepartment();
		}
		if (e.getSource() == book_list) {
			if (e.getClickCount() == 2)
				new updateBook();
		}
		if (e.getSource() == custmer_list) {
			if (e.getClickCount() == 2)
				new updateInfoCustomer();
		}

	}

	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void actionPerformed(ActionEvent e) {

		if (e.getSource() == close)
			this.setVisible(false);
		if (e.getSource() == dep_btn)
			new addNewDepartment();
		if (e.getSource() == book_btn)
			new addNewBook();
		if (e.getSource() == customer_btn)
			new addNewCustomer();

	}

}
