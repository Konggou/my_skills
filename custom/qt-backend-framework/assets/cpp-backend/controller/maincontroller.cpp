#include "maincontroller.h"
#include "../service/appservice.h"
#include "../model/appmodel.h"

MainController::MainController(QObject *parent)
    : QObject(parent)
    , m_app_service(new AppService(this))
    , m_app_model(new AppModel())
{
    connect(m_app_service, &AppService::WorkCompleted,
            this, &MainController::OnServiceWorkCompleted);
    connect(m_app_service, &AppService::ErrorOccurred,
            this, &MainController::OnServiceError);
}

MainController::~MainController()
{
    delete m_app_model;
}

void MainController::RequestDoWork(const QString &input)
{
    m_app_service->DoWork(input);
}

void MainController::OnServiceWorkCompleted(bool success, const QString &result)
{
    if (m_app_model)
        m_app_model->setStatus(success ? "ok" : "error");
    emit WorkCompleted(success, result);
}

void MainController::OnServiceError(const QString &message)
{
    if (m_app_model)
        m_app_model->setStatus("error");
    emit ErrorOccurred(message);
}
