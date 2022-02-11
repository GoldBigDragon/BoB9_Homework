#include "widget.h"
#include "ui_widget.h"
#include <QMessageBox>

Widget::Widget(QWidget *parent) : QWidget(parent), ui(new Ui::Widget) {
    ui->setupUi(this);
    changeMoney(0);
}

Widget::~Widget() {
    delete ui;
}

void Widget::on_put10_clicked() {
    changeMoney(10);
}

void Widget::on_put50_clicked() {
    changeMoney(50);
}

void Widget::on_put100_clicked() {
    changeMoney(100);
}

void Widget::on_put500_clicked() {
    changeMoney(500);
}

void Widget::on_put1000_clicked() {
    changeMoney(1000);
}

void Widget::on_buyCoffee_clicked() {
    changeMoney(-100);
}

void Widget::on_buyTea_clicked() {
    changeMoney(-150);
}

void Widget::on_buyMilk_clicked() {
    changeMoney(-200);
}

void Widget::on_buyCola_clicked() {
    changeMoney(-350);
}

void Widget::on_buyHot6_clicked() {
    changeMoney(-800);
}

void Widget::changeMoney(int diff){
    if(money+diff < 0) {
        return;
    }
    money += diff;
    ui->lcdNumber->display(money);
    bool coffee = false;
    bool tea = false;
    bool milk = false;
    bool cola = false;
    bool hot6 = false;
    if(money >= 100)
        coffee = true;
    if(money >= 150)
        tea = true;
    if(money >= 200)
        milk = true;
    if(money >= 350)
        cola = true;
    if(money >= 800)
        hot6 = true;
    ui->buyCoffee->setEnabled(coffee);
    ui->buyTea->setEnabled(tea);
    ui->buyMilk->setEnabled(milk);
    ui->buyCola->setEnabled(cola);
    ui->buyHot6->setEnabled(hot6);
}

void Widget::on_reset_clicked() {
    QString string = QString("거스름돈 %1원을 받았습니다!").arg(money);
    changeMoney(-money);
    QMessageBox m;
    m.information(nullptr, "잔액 반환", string);
}
