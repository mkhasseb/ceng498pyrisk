#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_mapView_destroyed()
{

}

void MainWindow::on_widget_customContextMenuRequested(QPoint pos)
{

}

void MainWindow::on_actionOpen_triggered()
{

}
