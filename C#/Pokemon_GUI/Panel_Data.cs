namespace cs_gui;
using System;
using System.Drawing;
using System.Windows.Forms;
using System.Data.SQLite;

public partial class Pic_Panel : Panel {
    public Pic_Panel() {
        this.BackColor = SystemColors.Window;
        this.ClientSize = new Size(1000, 700);
        this.Location = new Point(0, 0);
        set_status_button();
        option_status_layout();
    }

    #nullable disable
    public void option_status_layout() {
        // close_button.Click += form_close;

        this.Controls.AddRange(new Control[] {
            add_button,
            reset_button,
            close_button
        });
    }

    // パーツ生成
    private
    ListView pk_search_table = new ListView() {
        View = View.Details,
        GridLines = true,
        Size = new Size(850, 350),
        Location = new Point(75, 305)
    };
    Button add_button = new Button() {
        Name = "add",
        Text = "追加",
        Location = new Point(380, 265),
        Size = new Size(80, 20)
    };
    Button reset_button = new Button() {
        Name = "reset",
        Text = "リセット",
        Location = new Point(460, 265),
        Size = new Size(80, 20)
    };
    Button close_button = new Button() {
        Name = "Close",
        Text = "閉じる",
        Location = new Point(540, 265),
        Size = new Size(80, 20)
    };
    
    // ポケモン関係
    Label name_label = new Label() {
        Name = "Name",
        Text = "名前",
        Location = new Point(220, 50),
        Size = new Size(80, 25)
    };
    Label type1_label = new Label(){
        Name = "type1",
        Text = "タイプ1",
        Location = new Point(220, 75),
        Size = new Size(80, 25)
    };
    Label type2_label = new Label(){
        Name = "type2",
        Text = "タイプ2",
        Location = new Point(220, 100),
        Size = new Size(80, 25)
    };
    Label abi1_label = new Label(){
        Name = "abi1",
        Text = "特性1",
        Location = new Point(220, 125),
        Size = new Size(80, 25)
    };
    Label abi2_label = new Label(){
        Name = "abi2",
        Text = "特性2",
        Location = new Point(220, 150),
        Size = new Size(80, 25)
    };
    Label gene_label = new Label(){
        Name = "gene",
        Text = "世代",
        Location = new Point(220, 175),
        Size = new Size(80, 25)
    };
    Label class_label = new Label(){
        Name = "class",
        Text = "分類",
        Location = new Point(220, 200),
        Size = new Size(80, 25)
    };

    ComboBox name_button = new ComboBox(){
        Name = "Name",
        Text = "名前",
        Location = new Point(300, 50),
        Size = new Size(80, 25),
    };
    ComboBox type1_button = new ComboBox(){
        Name = "type1",
        Text = "タイプ1",
        Location = new Point(300, 75),
        Size = new Size(80, 25),
    };
    ComboBox type2_button = new ComboBox(){
        Name = "type2",
        Text = "タイプ2",
        Location = new Point(300, 100),
        Size = new Size(80, 25)
    };
    TextBox abi1_button = new TextBox(){
        Name = "abi1",
        Text = "特性1",
        Location = new Point(300, 125),
        Size = new Size(80, 25)
    };
    TextBox abi2_button = new TextBox(){
        Name = "abi2",
        Text = "特性2",
        Location = new Point(300, 150),
        Size = new Size(80, 25)
    };
    ComboBox gene_button = new ComboBox(){
        Name = "gene",
        Text = "世代",
        Location = new Point(300, 175),
        Size = new Size(80, 25)
    };
    ComboBox class_button = new ComboBox(){
        Name = "class",
        Text = "分類",
        Location = new Point(300, 200),
        Size = new Size(80, 25)
    };

    Label status_upper_SUM = new Label(){
        Name = "以上",
        Text = "以上",
        Location = new Point(540, 50),
        Size = new Size(80, 25)
    };
    Label status_upper_H = new Label(){
        Name = "以上",
        Text = "以上",
        Location = new Point(540, 75),
        Size = new Size(80, 25)
    };
    Label status_upper_A = new Label(){
        Name = "以上",
        Text = "以上",
        Location = new Point(540, 100),
        Size = new Size(80, 25)
    };
    Label status_upper_B = new Label(){
        Name = "以上",
        Text = "以上",
        Location = new Point(540, 125),
        Size = new Size(80, 25)
    };
    Label status_upper_C = new Label(){
        Name = "以上",
        Text = "以上",
        Location = new Point(540, 150),
        Size = new Size(80, 25)
    };
    Label status_upper_D = new Label(){
        Name = "以上",
        Text = "以上",
        Location = new Point(540, 175),
        Size = new Size(80, 25)
    };
    Label status_upper_S = new Label(){
        Name = "以上",
        Text = "以上",
        Location = new Point(540, 200),
        Size = new Size(80, 25)
    };
    
    Label status_lower_SUM = new Label(){
        Name = "以下",
        Text = "以下",
        Location = new Point(700, 50),
        Size = new Size(80, 25)
    };
    Label status_lower_H = new Label(){
        Name = "以下",
        Text = "以下",
        Location = new Point(700, 75),
        Size = new Size(80, 25)
    };
    Label status_lower_A = new Label(){
        Name = "以下",
        Text = "以下",
        Location = new Point(700, 100),
        Size = new Size(80, 25)
    };
    Label status_lower_B = new Label(){
        Name = "以下",
        Text = "以下",
        Location = new Point(700, 125),
        Size = new Size(80, 25)
    };
    Label status_lower_C = new Label(){
        Name = "以下",
        Text = "以下",
        Location = new Point(700, 150),
        Size = new Size(80, 25)
    };
    Label status_lower_D = new Label(){
        Name = "以下",
        Text = "以下",
        Location = new Point(700, 175),
        Size = new Size(80, 25)
    };
    Label status_lower_S = new Label(){
        Name = "以下",
        Text = "以下",
        Location = new Point(700, 200),
        Size = new Size(80, 25)
    };
    Label status_text_SUM = new Label(){
        Name = "SUM",
        Text = "合計値",
        Location = new Point(380, 50),
        Size = new Size(80, 25),
    };
    Label status_text_H = new Label(){
        Name = "H",
        Text = "HP",
        Location = new Point(380, 75),
        Size = new Size(80, 25),
    };
    Label status_text_A = new Label(){
        Name = "A",
        Text = "攻撃",
        Location = new Point(380, 100),
        Size = new Size(80, 25),
    };
    Label status_text_B = new Label(){
        Name = "B",
        Text = "防御",
        Location = new Point(380, 125),
        Size = new Size(80, 25),
    };
    Label status_text_C = new Label(){
        Name = "C",
        Text = "特攻",
        Location = new Point(380, 150),
        Size = new Size(80, 25),
    };
    Label status_text_D = new Label(){
        Name = "D",
        Text = "特防",
        Location = new Point(380, 175),
        Size = new Size(80, 25),
    };
    Label status_text_S = new Label(){
        Name = "S",
        Text = "素早さ",
        Location = new Point(380, 200),
        Size = new Size(80, 25),
    };

    TextBox status_m_SUM = new TextBox(){
        Name = "SUM",
        Text = "0",
        Location = new Point(460, 50),
        Size = new Size(80, 25),
    };
    TextBox status_m_H = new TextBox(){
        Name = "H",
        Text = "0",
        Location = new Point(460, 75),
        Size = new Size(80, 25),
    };
    TextBox status_m_A = new TextBox(){
        Name = "A",
        Text = "0",
        Location = new Point(460, 100),
        Size = new Size(80, 25),
    };
    TextBox status_m_B = new TextBox(){
        Name = "B",
        Text = "0",
        Location = new Point(460, 125),
        Size = new Size(80, 25),
    };
    TextBox status_m_C = new TextBox(){
        Name = "C",
        Text = "0",
        Location = new Point(460, 150),
        Size = new Size(80, 25),
    };
    TextBox status_m_D = new TextBox(){
        Name = "D",
        Text = "0",
        Location = new Point(460, 175),
        Size = new Size(80, 25),
    };
    TextBox status_m_S = new TextBox(){
        Name = "S",
        Text = "0",
        Location = new Point(460, 200),
        Size = new Size(80, 25),
    };
    
    TextBox status_M_SUM = new TextBox(){
        Name = "sum",
        Text = "255",
        Location = new Point(620, 50),
        Size = new Size(80, 25),
    };
    TextBox status_M_H = new TextBox(){
        Name = "H",
        Text = "255",
        Location = new Point(620, 75),
        Size = new Size(80, 25),
    };
    TextBox status_M_A = new TextBox(){
        Name = "A",
        Text = "255",
        Location = new Point(620, 100),
        Size = new Size(80, 25),
    };
    TextBox status_M_B = new TextBox(){
        Name = "B",
        Text = "255",
        Location = new Point(620, 125),
        Size = new Size(80, 25),
    };
    TextBox status_M_C = new TextBox(){
        Name = "C",
        Text = "255",
        Location = new Point(620, 150),
        Size = new Size(80, 25),
    };
    TextBox status_M_D = new TextBox(){
        Name = "D",
        Text = "255",
        Location = new Point(620, 175),
        Size = new Size(80, 25),
    };
    TextBox status_M_S = new TextBox(){
        Name = "S",
        Text = "255",
        Location = new Point(620, 200),
        Size = new Size(80, 25),
    };

    public void set_status_button () {
        this.Controls.AddRange(new Control[] {
            name_label,
            type1_label,
            type2_label,
            abi1_label,
            abi2_label,
            gene_label,
            class_label,
            name_button,
            type1_button,
            type2_button,
            abi1_button,
            abi2_button,
            gene_button,
            class_button,
        });
        this.Controls.AddRange(new Control[] {
            status_text_SUM,
            status_text_H,
            status_text_A,
            status_text_B,
            status_text_C,
            status_text_D,
            status_text_S,
            status_upper_SUM,
            status_upper_H,
            status_upper_A,
            status_upper_B,
            status_upper_C,
            status_upper_D,
            status_upper_S,
            status_lower_SUM,
            status_lower_H,
            status_lower_A,
            status_lower_B,
            status_lower_C,
            status_lower_D,
            status_lower_S,
            status_m_SUM,
            status_m_H,
            status_m_A,
            status_m_B,
            status_m_C,
            status_m_D,
            status_m_S,
            status_M_SUM,
            status_M_H,
            status_M_A,
            status_M_B,
            status_M_C,
            status_M_D,
            status_M_S,            
        });

        this.Controls.Add(pk_search_table);
    }

    string[] type_name_list = new string[] {"ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり", "かくとう", "どく", "じめん", "ひこう", "エスパー", "むし", "いわ", "ゴースト", "ドラゴン", "あく", "はがね", "フェアリー"};

    // public void form_close (object sender, EventArgs e) {
    //     this.Close();
    // }
}

