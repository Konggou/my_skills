#include "mainwindow.h"
#include <QWidget>
#include <QVBoxLayout>
#include <QLabel>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    SetupUI();
    ConnectSignals();
}

MainWindow::~MainWindow()
{
}

void MainWindow::SetupUI()
{
    QWidget *central_widget = new QWidget(this);
    setCentralWidget(central_widget);

    QVBoxLayout *layout = new QVBoxLayout(central_widget);

    QLabel *label = new QLabel("Hello, Qt!", this);
    layout->addWidget(label);

    setWindowTitle("My Application");
    resize(800, 600);
}

void MainWindow::ConnectSignals()
{
    // Connect signals and slots here.
    // Example: connect(button, &QPushButton::clicked, this, &MainWindow::OnButtonClicked);
}
