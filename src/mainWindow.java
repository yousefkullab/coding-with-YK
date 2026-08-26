import java.awt.Container;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class mainWindow extends JFrame implements ActionListener {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	Container c;
	JPanel pnl = new JPanel();
	JComboBox<Object> box;
	String s[] = { "Calculator", "Metric Converter" };
	JButton btn = new JButton("Go");

	public mainWindow() {
		c = getContentPane();
		setLayout(null);

		pnl.setLayout(null);
		pnl.setBounds(0, 0, 400, 350);
		box = new JComboBox<Object>(s);
		box.setBounds(30, 120, 200, 30);
		box.setSelectedIndex(0);
		box.setFont(new Font("Dialog", Font.BOLD, 20));

		btn.setBounds(250, 120, 100, 30);
		btn.setFont(new Font("Dialog", Font.BOLD, 20));
		btn.addActionListener(this);

		pnl.add(box);
		pnl.add(btn);
		c.add(pnl);

		setSize(400, 350);
		setLocationRelativeTo(null);
		setVisible(true);

	}

	public static void main(String[] args) {

		new mainWindow();

	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if ((e.getSource() == btn) && (box.getSelectedItem().equals("Calculator")))
			new Calculater();
		else
			new MetricConverter();

	}

}
// Software Engineer Joseph . 20202273