import java.util.*;
interface Detail{
    public void details();
    public void showFare(int vehicle_type,double distance);
    public void setPayment_option(int payment_option);
}
class DistanceCalculator {
    private final int EARTH_RADIUS_KM = 6371; // Earth's mean radius in kilometers
    double latS;
    double longS;
    double latD;
    double longD;
    public double latlong(String source, String destination){
        if(source.replaceAll("\\s+","").equalsIgnoreCase("somaiyavidyavihar")){
            latS=19.0728;
            longS=72.8999;
        }if(destination.replaceAll("\\s+","").equalsIgnoreCase("somaiyavidyavihar")){
            latD=19.0728;
            longD=72.8999;
        }if(source.replaceAll("\\s+","").equalsIgnoreCase("airportt1")){
            latS=19.0886;
            longS=72.8681;
        }if(destination.replaceAll("\\s+","").equalsIgnoreCase("airportt1")){
            latD=19.0886;
            longD=72.8681;
        }if(source.replaceAll("\\s+","").equalsIgnoreCase("airportt2")){
            latS=19.0887;
            longS=72.8679;
        }if(destination.replaceAll("\\s+","").equalsIgnoreCase("airportt2")){
            latD=19.0887;
            longD=72.8679;
        }if(source.replaceAll("\\s+","").equalsIgnoreCase("navimumbaiairport")){
            latS=19.9914;//Recheck
            longS=72.86166;
        }if(destination.replaceAll("\\s+","").equalsIgnoreCase("navimumbaiairport")){
            latD=19.9914;//Recheck
            longD=72.86166;
        }
        if(source.replaceAll("\\s+","").equalsIgnoreCase("GhatkoparMetroStation")){
            latS = 19.0866409;
            longS = 72.9079905;
        }
        if(source.replaceAll("\\s+","").equalsIgnoreCase("GhatkoparRailwayStation")){
            latS = 19.08569;
            longS = 72.90837;
        }
        if(source.replaceAll("\\s+","").equalsIgnoreCase("VidyaViharRailwayStation")){
            latS = 19.0796294;
            longS = 72.8974907;
        }
        if(source.replaceAll("\\s+","").equalsIgnoreCase("TilakNagarRailwayStation")){
            latS = 19.067312;
            longS = 72.888481;
        } if(destination.replaceAll("\\s+","").equalsIgnoreCase("GhatkoparMetroStation")){
            latD = 19.0866409;
            longD = 72.9079905;
        }
        if(destination.replaceAll("\\s+","").equalsIgnoreCase("GhatkoparRailwayStation")){
            latD = 19.08569;
            longD = 72.90837;
        }
        if(destination.replaceAll("\\s+","").equalsIgnoreCase("VidyaViharRailwayStation")){
            latD = 19.0796294;
            longD = 72.8974907;
        }
        if(destination.replaceAll("\\s+","").equalsIgnoreCase("TilakNagarRailwayStation")){
            latD = 19.067312;
            longD = 72.888481;
        }

        return calculateDistance(latS,longS,latD,longD);
    }
    public double calculateDistance(double lat1, double lon1, double lat2, double lon2) {
        double latDistance = Math.toRadians(lat2 - lat1);
        double lonDistance = Math.toRadians(lon2 - lon1);

        double a = Math.sin(latDistance / 2) * Math.sin(latDistance / 2)
                + Math.cos(Math.toRadians(lat1)) * Math.cos(Math.toRadians(lat2))
                * Math.sin(lonDistance / 2) * Math.sin(lonDistance / 2);

        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

        return EARTH_RADIUS_KM * c; // Distance in kilometers
    }
}
class Passenger implements Detail{
    private String source;
    private String destination;
    private int vehicle_type;
    private double fare;
    private int payment_option;
    private double distance;
    private String upi_id;
    private int upi_pin;
    private int card_num;
    private int cvv;
    private int card_pin;
    @Override
    public void details() {
        Scanner in = new Scanner(System.in);
        System.out.println("Please enter source:");
        source = in.nextLine();
        System.out.println("Please enter the destination:");
        destination = in.nextLine();
        DistanceCalculator dc = new DistanceCalculator();
        distance = dc.latlong(source, destination);
        System.out.println("Please enter \n1.Mini\n2.Sedan\n3.SUV:");
        vehicle_type = in.nextInt();
        showFare(vehicle_type, distance);
        System.out.println("Please enter \n1.UPI\n2.Credit Card:");
        payment_option = in.nextInt();
        setPayment_option(payment_option);
    }
    @Override
    public void setPayment_option(int payment_option) {
        Scanner in=new Scanner(System.in);
        in.nextLine();
        do{
        if (payment_option == 1) {
            System.out.println("Please enter your UPI id:");
            upi_id = in.nextLine();
            System.out.println("Please enter your UPI pin:");
            upi_pin = in.nextInt();
            System.out.println("Payment Successful!");
            System.out.println("Your ride will be at your location in a few minutes.");
        } else if (payment_option == 2) {
            System.out.println("Please enter your card number:");
            card_num = in.nextInt();
            System.out.println("Please enter your CVV:");
            cvv = in.nextInt();
            System.out.println("Please enter your pin:");
            card_pin = in.nextInt();
            System.out.println("Payment Successful!");
            System.out.println("Your ride will be at your location in a few minutes.");
        }
        else{
            System.out.println("Error!");
        }
        }while(payment_option>2&&payment_option<0);
    }
    @Override
    public void showFare(int vehicle_type,double distance){
        do{
        switch (vehicle_type) {
            case 1:
                fare = Math.ceil(30 + (3 * distance));
                System.out.println("Total fare is " + fare + ".");
                break;
            case 2:
                fare = Math.ceil(30 + (4 * distance));
                System.out.println("Total fare is " + fare + ".");
                break;
            case 3:
                fare = Math.ceil(40 + (5 * distance));
                System.out.println("Total fare is " + fare + ".");
                break;
            default:
                System.out.println("Please enter a valid input.");
        }
        }while(vehicle_type>3||vehicle_type<0);
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        Passenger p=new Passenger();
        p.details();
    }
}
