%clear; clc; 

gt_path = '/Users/hsin-hung.chen/Documents/HH document/Gatech MT/7100/VAreMixer-master/music_source/gt_mix_medley_filt/';
sep_path = '/Users/hsin-hung.chen/Documents/HH document/Gatech MT/7100/VAreMixer-master/music_source/sep_mix_wiener_filt/';
re_path = '/Users/hsin-hung.chen/Documents/HH document/Gatech MT/7100/VAreMixer-master/music_source/remix_wiener_filt/';


%odg_path = '/Users/hsin-hung.chen/Documents/HH document/Gatech MT/7100/VAreMixer-master/music_source/odg_filt_lowpass_0p9/';
odg_path = '/Users/hsin-hung.chen/Documents/HH document/Gatech MT/7100/VAreMixer-master/music_source/odg_filt_zero_highpass_0p8/';


for i = 1:800

    gt_mix_path = append(gt_path, int2str(i))
    sep_mix_path = append(sep_path, int2str(i))
    remix_path = append(re_path, int2str(i))
    odg_impr_path = append(odg_path, int2str(i))
    
    gt_mix_files = dir(gt_mix_path);
    sep_mix_files = dir(sep_mix_path);
    remix_files = dir(remix_path);
    f = fopen(odg_impr_path,'w');

    odg_arr = [];

    for k = 3:length(remix_files) 
       gt_FileNames = gt_mix_files(k).name
       gt_filepath = fullfile(gt_mix_path, gt_FileNames);
       sep_FileNames = sep_mix_files(k).name
       sep_filepath = fullfile(sep_mix_path, sep_FileNames);
       re_FileNames = remix_files(k).name
       re_filepath = fullfile(remix_path, re_FileNames);

       odg_improve = peaq_remix_odg(gt_filepath, sep_filepath, re_filepath);
       if k == 4
          odg_10_0 = odg_improve;
       else
          odg_arr = [odg_arr odg_improve];
          fprintf(f,'%f\n', odg_improve);
       end
    end

    odg_arr = [odg_arr odg_10_0]
    fprintf(f,'%f\n', odg_10_0);
    fclose(f);
end

%fileID = fopen('exp.txt','w');
%fprintf(fileID,'%6s %12s\n','x','exp(x)');
%fprintf(fileID,'%6.2f %12.8f\n',A);
%fclose(fileID);