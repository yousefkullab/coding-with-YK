import java.awt.Color;
import java.awt.Container;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;

public class updateBook extends JFrame implements ActionListener {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	Container c;
	JButton close = new JButton("X");
	JLabel updateNew = new JLabel("Update Book");

	JLabel bookName = new JLabel("Book Name : ");
	JTextField bookName_txt = new JTextField();
	JLabel price = new JLabel("Price : ");
	JTextField price_txt = new JTextField();
	JLabel copies = new JLabel("No.Copies : ");
	JTextField copies_txt = new JTextField();
	JLabel author = new JLabel("Author : ");
	JTextField author_txt = new JTextField();
	JLabel isbn = new JLabel("ISBN : ");
	JTextField isbn_txt = new JTextField();
	JLabel dep = new JLabel("Department : ");
	JComboBox<Object> dep_box = new JComboBox<Object>();
	JLabel sign = new JLabel("$");

	JButton update_btn = new JButton("Update Book");
	JButton cancel = new JButton("Cancel");

	public updateBook() {
		c = getContentPane();
		getContentPane().setBackground(new Color(209, 232, 240));
		setLayout(null);
		bookName.setBounds(40, 100, 150, 30);
		bookName.setForeground(new Color(62, 119, 185));
		bookName_txt.setBounds(120, 100, 250, 30);
		price.setBounds(40, 150, 150, 30);
		price.setForeground(new Color(62, 119, 185));
		price_txt.setBounds(120, 150, 100, 30);
		sign.setBounds(225, 150, 100, 30);
		sign.setForeground(new Color(62, 119, 185));
		sign.setFont(new Font("Comic Sans MS", Font.BOLD, 18));
		copies.setBounds(40, 200, 100, 30);
		copies.setForeground(new Color(62, 119, 185));
		copies_txt.setBounds(120, 200, 100, 30);
		author.setBounds(40, 250, 200, 30);
		author.setForeground(new Color(62, 119, 185));
		author_txt.setBounds(120, 250, 200, 30);
		isbn.setBounds(40, 300, 200, 30);
		isbn.setForeground(new Color(62, 119, 185));
		isbn_txt.setBounds(120, 300, 200, 30);
		dep.setBounds(40, 350, 100, 30);
		dep.setForeground(new Color(62, 119, 185));
		dep_box.setBounds(120, 350, 150, 30);

		close.setBounds(550, 5, 45, 45);
		close.setForeground(new Color(62, 119, 185));
		close.setBackground(new Color(209, 232, 240));
		close.setBorder(null);
		close.setFocusPainted(false);
		close.addActionListener(this);
		updateNew.setBounds(230, 30, 200, 30);
		updateNew.setFont(new Font("Comic Sans MS", Font.BOLD, 17));

		update_btn.setBounds(70, 430, 200, 30);
		update_btn.addActionListener(this);
		cancel.setBounds(330, 430, 150, 30);
		cancel.addActionListener(this);

		c.add(bookName);
		c.add(bookName_txt);
		c.add(price);
		c.add(price_txt);
		c.add(sign);
		c.add(copies);
		c.add(copies_txt);
		c.add(author);
		c.add(author_txt);
		c.add(isbn);
		c.add(isbn_txt);
		c.add(dep);
		c.add(dep_box);
		c.add(update_btn);
		c.add(cancel);
		c.add(updateNew);
		c.add(close);

		setSize(600, 500);
		setUndecorated(true);
		setLocationRelativeTo(null);
		setVisible(true);
		setResizable(false);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

	}

	public static void main(String[] args) {
		new updateBook();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == close)
			this.setVisible(false);
		if (e.getSource() == cancel)
			this.setVisible(false);
		if (e.getSource() == update_btn) {
			setVisible(false);
			JOptionPane.showMessageDialog(this, "Update book susscefly");
		}

	}

}
