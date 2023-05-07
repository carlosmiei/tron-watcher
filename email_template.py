def get_html_body(account, id, action, amount, date, link, other_key, other_account):
  return f'''
<table border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width:100%;" class="yiv6963182806mcnTextBlock">
    <tbody class="yiv6963182806mcnTextBlockOuter">
       <tr>
          <td valign="top" style="padding-top:9px;" class="yiv6963182806mcnTextBlockInner">
             <table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%;min-width:100%;" width="100%" class="yiv6963182806mcnTextContentContainer">
                <tbody>
                   <tr>
                      <td valign="top" style="padding:0px 18px 9px;">
                         <div style="text-align:left;font-size:14px;">
                            <p>Dear valued user,</p>
                            <p>Your  <b>{action}</b> has been confirmed.</p>
                            <p>{action} amount: <b>{amount} USDT</b></p>
                            <p>Account address: <b>{account}</b></p>
                            <p>{other_key} address: <b>{other_account}</b></p>
                            <p>Timestamp: <b>{date} </b></p>
                            <p>Id: <b>{id} </b></p>
                            <p>Tron explorer: <a href="{link}">link</a> </p>
                            <p></p>
                            <p></p>
                            <p></p>
                            <p>Regards,</p>
                            <p>Your dear watcher bot!</p>
                         </div>
                      </td>
                   </tr>
                </tbody>
             </table>
          </td>
       </tr>
    </tbody>
 </table>
'''