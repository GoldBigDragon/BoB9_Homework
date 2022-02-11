#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

QT_BEGIN_NAMESPACE
namespace Ui { class Widget; }
QT_END_NAMESPACE

class Widget : public QWidget
{
    Q_OBJECT
    int money {0};
    void changeMoney(int diff);

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

private slots:
    void on_put100_clicked();

    void on_put500_clicked();

    void on_buyCoffee_clicked();

    void on_buyTea_clicked();

    void on_buyMilk_clicked();

    void on_reset_clicked();

    void on_put1000_clicked();

    void on_put10_clicked();

    void on_put50_clicked();

    void on_buyCola_clicked();

    void on_buyHot6_clicked();

private:
    Ui::Widget *ui;
};
#endif // WIDGET_H
