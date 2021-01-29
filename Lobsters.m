% Name: Lobsters.m
% Author: Arnold Wright
% Date: 2021-01-28
% Explanation: Lobster numbers are composite numbers where all the prime
% factors of the number can be found as subsequences of the number.
% The Strong variant requires that all the factors can be found
% simultaneously without using a digit more than once. 

clear all;
clc;
tic;
for i=1:4294967295
    if ~isprime(i)
        if isequal(sort(strrep(num2str(factor(i)),' ','')),sort(strrep(num2str(i),' ',''))) % has all correct values
            % then do slow check for correct order
            f=factor(i);
            lf=size(f,2);
            n=num2str(i);
            ln=strlength(n);
            subs=zeros(1,2,ln);
            for j=1:(2^ln)-1 % iterate through all possible subsequences
                js=dec2bin(j,ln);
                tempsubs=0;
                for k=1:ln % for each digit
                    if js(k)=="1"
                        tempsubs=tempsubs*10 + (n(k)-'0'); % create the subsequence
                    end
                end
                % then check which substrings match factors
                if any(tempsubs==f)
                        subs(j,2,:)=js-'0'; % store binary mask
                        subs(j,1)=tempsubs; % store value
                end
            end
            trimsubs=subs(subs(:,1)>0,:,:);
            % create all possible combinations of the different matches
            trimsize=size(trimsubs,1);
            for j=1:(2^trimsize)-1 % iterate through all possible subsequences
                js=dec2bin(j,trimsize);
                tempmat=zeros(trimsize,2,ln);
                for k=1:trimsize
                    if js(k)=="1"
                        tempmat(k,:,:)=trimsubs(k,:,:); % create the subsequence
                    end
                end
                % check if it contains all matches
                trimmat=tempmat(tempmat(:,1)>0,:,:);
                if size(trimmat,1)==lf
                    if sort(trimmat(:,1,1))'==sort(f)
                        % if it does, then check if the binary masks are valid to coexist
                        if all(sum(trimmat(:,2,:),1)<=1)
                            fprintf("\n%d with factors: ",i);
                            fprintf("%d ",f);
                            fprintf("\n");
                        end
                    end
                end
            end
        end
    end
    if mod(i,10000)==0
        fprintf(".");
    end
    if mod(i,1000000)==0
        toc;
    end
end


