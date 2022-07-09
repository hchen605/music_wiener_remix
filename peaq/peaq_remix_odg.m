
function odg_impr = peaq_remix_odg(gt, mix, remix)

%ref = '/Users/hsin-hung.chen/Documents/HH document/Gatech MT/7100/VAreMixer-master/Supplementary Material/remix example/example_0/s1_5:s2_5.wav'
%test = '/Users/hsin-hung.chen/Documents/HH document/Gatech MT/7100/VAreMixer-master/Supplementary Material/remix example/example_0/s1_5:s2_5.wav'


[odg_mix, movb] = PQevalAudio_fn(gt, mix);
[odg_remix, movb] = PQevalAudio_fn(gt, remix);

odg_impr = odg_remix - odg_mix;
