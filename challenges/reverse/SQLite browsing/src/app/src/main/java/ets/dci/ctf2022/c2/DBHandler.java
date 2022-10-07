package ets.dci.ctf2022.c2;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class DBHandler extends SQLiteOpenHelper {
    // creating a constant variables for our database.
    // below variable is for our database name.
    private static final String DB_NAME = "coursedb";

    // below int is our database version
    private static final int DB_VERSION = 1;

    // below variable is for our table name.
    private static final String COURSE_NAME = "Courses";

    // below variable is for our id column.
    private static final String ID_COL = "id";

    // below variable is for our course name column
    private static final String NAME_COL = "name";

    // creating a constructor for our database handler.
    public DBHandler(Context context) {
        super(context, DB_NAME, null, DB_VERSION);
}

    @Override
    public void onCreate(SQLiteDatabase sqLiteDatabase) {
        String query = "CREATE TABLE " + COURSE_NAME + " ("
                + ID_COL + " INTEGER PRIMARY KEY AUTOINCREMENT, "
                + NAME_COL + " TEXT)";

        sqLiteDatabase.execSQL(query);

        String query2 = "CREATE TABLE Flag ("
                + ID_COL + " INTEGER PRIMARY KEY AUTOINCREMENT, "
                + "flag TEXT)";

        sqLiteDatabase.execSQL(query2);

        addNewCourses(sqLiteDatabase);
        addFlag(sqLiteDatabase);
    }

    @Override
    public void onUpgrade(SQLiteDatabase sqLiteDatabase, int i, int i1) {
        // this method is called to check if the table exists already.
        sqLiteDatabase.execSQL("DROP TABLE IF EXISTS " + COURSE_NAME);
        onCreate(sqLiteDatabase);
    }

    // this method is use to add new course to our sqlite database.
    private void addNewCourses(SQLiteDatabase sqLiteDatabase) {
        for (String cours : Constants.courses) {
            ContentValues values = new ContentValues();
            values.put(NAME_COL, cours);
            sqLiteDatabase.insert(COURSE_NAME, null, values);
        }
    }

    // this method is use to search in the sqlite DB securely
    public String search(String searchTerm) {
        SQLiteDatabase db = this.getReadableDatabase();
        StringBuilder sb = new StringBuilder();

        try {
            Cursor c = db.rawQuery("SELECT " + NAME_COL + " FROM " + COURSE_NAME + " WHERE " + NAME_COL + " =?", new String[] { searchTerm });

            if (c.moveToFirst()){
                do {
                    String name = c.getString(0);
                    sb.append(name);
                    sb.append("\n");
                } while(c.moveToNext());
            }
            db.close();
            return sb.toString();
        } catch (Exception e) {
            System.err.println(e);
            return "Impossible to parse search. Sorry...";
        }
    }

    // this method is use to add new course to our sqlite database.
    private void addFlag(SQLiteDatabase sqLiteDatabase) {
        ContentValues values = new ContentValues();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < Constants.key.length(); i++) {
            sb.append(Constants.key.charAt(Constants.key.length() - i - 1));
        }

        MessageDigest md = null;
        String hashtext = "";
        try {
            byte[] bytesOfMessage = sb.toString().getBytes("UTF-8");
            md = MessageDigest.getInstance("MD5");
            byte[] digest = md.digest(bytesOfMessage);
            BigInteger bigInt = new BigInteger(1, digest);
            hashtext = bigInt.toString(16);
        } catch (NoSuchAlgorithmException | UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        System.out.println(hashtext);
        values.put("flag", "FLAG-" + hashtext);
        sqLiteDatabase.insert("Flag", null, values);
    }

}
