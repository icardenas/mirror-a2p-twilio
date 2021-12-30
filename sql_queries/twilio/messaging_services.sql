--Check if MS is repeat
select tmm.id, tmm.sid, tmm.friendly_name, p.friendly_name
from twilio_management_messagingservice tmm
         left join twilio_management_phonenumber p on tmm.id = p.messaging_service_id
where tmm.friendly_name in (select ms.friendly_name
                            from twilio_management_messagingservice ms
                                     left join twilio_management_compliance tmc on ms.id = tmc.messaging_service_id
                                     left join twilio_management_phonenumber tmp on ms.id = tmp.messaging_service_id
                            where tmc.id is null
                              and tmp.id is null)
ORDER BY 3 desc;

---Check MS without embedded_phone or link in the campaign (wrong configuration)
select tmc.sid, tmc.us_app_to_person_usecase, tmc.campaign_id, tmc.campaign_status, tmc.has_embedded_phone, tmc.has_embedded_links,
       tmm.sid, tmm.friendly_name, tmm.inbound_method, tmm.inbound_request_url, tmm.use_inbound_webhook_on_number
from twilio_management_compliance tmc
         join twilio_management_messagingservice tmm on tmc.messaging_service_id = tmm.id
where tmc.has_embedded_phone is false or tmc.has_embedded_links=false;