select tmm.friendly_name, tmm.sid, tmp.phone_number, tmp.friendly_name
from twilio_management_a2pbrand a2p
         join twilio_management_brandregistration tmb on a2p.id = tmb.a2p_brand_id
         join twilio_management_compliance tmc on tmb.sid = tmc.brand_registration_sid
         join twilio_management_messagingservice tmm on tmc.messaging_service_id = tmm.id
        join twilio_management_phonenumber tmp on tmm.id = tmp.messaging_service_id
    where a2p.friendly_name = 'Apploi Holdings Inc.'
GROUP BY 1,2,3,4