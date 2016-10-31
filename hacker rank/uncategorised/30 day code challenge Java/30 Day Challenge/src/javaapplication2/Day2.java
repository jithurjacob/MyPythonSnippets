/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication2;

import java.util.Scanner;
import java.lang.Math.*;
/**
 *
 * @author Jithu R Jacob
 */
public class Day2 {
    public static void main(String args[]){
        
        Scanner in=new Scanner(System.in);
        Double M=in.nextDouble();
        int T=in.nextInt();
        int X=in.nextInt();
        
        System.out.print("The final price of the meal is $"+Math.round(M+(M*T)/100+(M*X)/100)+".");
    
    }
}
