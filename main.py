import os

def procurar_palavras_em_arquivos(diretorio, palavras):
    # Lista para armazenar os arquivos que contêm as palavras
    arquivos_encontrados = []

    # Navegar pelo diretório e seus subdiretórios
    for pasta_atual, subpastas, arquivos in os.walk(diretorio):
        for nome_arquivo in arquivos:
            caminho_completo = os.path.join(pasta_atual, nome_arquivo)

            try:
                # Tentar abrir o arquivo e verificar se todas as palavras estão nele
                with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
                    conteudo = arquivo.read()
                    for p in palavras:
                        if p in conteudo:
                            arquivos_encontrados.append([caminho_completo, p])
            except UnicodeDecodeError:
                print(f"Ignorando o arquivo '{caminho_completo}' devido a um erro de decodificação Unicode.")

    return arquivos_encontrados

if __name__ == '__main__':
    palavra_alvo = 'sua_palavra'
    palavras_alvo = [
        'ChangePasswordIntranet',
        'SendConfirmationEcommerce',
        'SendEcommerceCancellationRequest',
        'SendEcommerceErroCancellationRequest',
        'SendEcommerceCancellationRequestOnlyCentral',
        'SendEcommerceEstabBlock',
        'SendEcommerceErroBilletGenerationRequest',
        'SendEcommerceCancellationApproveRequest',
        'SendTokensEcommerce',
        'SendEcommerce',
        'SendAttEcommerce',
        'SendPasswordRecovery',
        'SendLoginClient',
        'SendResetPasswordClient',
        'SendSms',
        'SendSmsFinish',
        'SendSolicitation',
        'SendSolicitationAnticipacao',
        'SendFichaCredenciamento',
        'SendContestacaoVendas',
        'SendSolicitacaoAntecipacaoRecebida',
        'SendChipsLowAlert',
        'SendTerminalsLowAlert',
        'SendSolicitacaoAntecipacaoConfirmada',
        'SendEmailBilletErrorToDev',
        'SignatureAdesaoCliente',
        'SendEmailExpireSignature',
        'SendEmailPaymentSignature',
        'SignatureChangeCard',
        'SendEmailChargeMadeSignature',
        'SendEmailChargeFailureSignatureToDev',
        'SendEmailSuspendedInactiveSignature',
        'SendEmailActiveSignature',
        'SendEmailChargeFailureSignature',
        'SendEmailChangeSignature',
        'SendEmailSignatureBilletRecurrence',
        'SendInvoiceCreate',
        'SendEmailCanceledInvoice',
        'SendEmailSolicitationCanceledInvoice',
        'SendEmailApprovedPaymentInvoice',
        'SendEmailReminderInvoice',
        'SendEmailOverdueInvoice',
        'SendEmailBillingWithErro',
        'SearchIntegracoes',
        'ClientCount',
        'ReleaseContract',
        'ChangeNumberPhoneFixPayEmailMarketing',
        'EmailWhatsaap',
        'InstabilitySystem',
        'CorrectemailInstabilitySystem',
        'EmailVivo',
        'CorrectEmailVivo',
        'EmailClaro',
        'CorrectEmailClaro',
        'CustomEmail',
        'PortalOut',
        'SendEmailCancelamentoTransacaoAdiquirente',
        'SendEmailVendaDigitada',
        'SendConfirmationLinkPayment',
        'SendCancellationRequestLinkPayment',
        'SendCancellationApproveRequestLinkPayment',
        'SendConfirmationLinkItems',
        'SendCancellationRequestLinkItems',
        'SendCancellationApproveRequestLinkItems',
        'SendConfirmationLinkPayment3DS',
        'SendCancellationRequestLinkPayment3DS',
        'SendCancellationApproveRequestLinkPayment3DS',
        'SendConfirmationLinkItems3DS',
        'SendCancellationRequestLinkItems3DS',
        'SendCancellationApproveRequestLinkItems3DS',
        'DaylyChangeReports',
        'SendSalesSitef',
        'SendSalesPayGo',
        'SendTransacoesSemCaptura',
        'SendEmailVerifyTerminal',
        'SendEmailCarteira',
        'SendEmailRelatorioVendas',
        'ErrorsPixItau',
        'BlockedCustomers',
        'SendComprovantePagamentoFixCar',
        'SendCancellationRequestLinkPaymentWallet',
        'SendConfirmationLinkPaymentWallet',
        'SendCancellationApproveRequestLinkPaymentWallet',
    ]

    # Chamar a função e obter a lista de arquivos encontrados
    arquivos_encontrados = procurar_palavras_em_arquivos("/home/gui/Documentos/fixpay/robo-cerc",  palavras_alvo)

    # Imprimir os resultados
    if arquivos_encontrados:
        print(f"Arquivos que contêm a palavra '{palavra_alvo}':")
        for arquivo in arquivos_encontrados:
            print(arquivo)
    else:
        print(f"Nenhum arquivo encontrado com a palavra '{palavra_alvo}'.")

